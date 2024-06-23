import numpy as np

minkowski_metric = np.diag([1,-1,-1,-1])

def gamma(v):
    return np.sqrt(1/(1-v**2))

class Frame:
    
    def __init__(self, lab_lorentz):
        # lab_lorentz is the nxn matrix gets us from the lab frame to the frame we're working in
        #if ((lab_lorentz.T).dot(minkowski_metric).dot(lab_lorentz) != minkowski_metric).any():
        #   raise TypeError("lab_lorentz is not a Lorentz transform (failed to preserve minkowski_metric)")
        self.lab_lorentz = lab_lorentz

    def equals(self, frame):
        return (self.lab_lorentz == frame.lab_lorentz).all()

    def boost_x(self, v):
        g = gamma(v)
        boosted_lorentz = np.array([[g, -g*v, 0, 0],
                           [-g*v, g, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]]).dot(self.lab_lorentz)
        return Frame(boosted_lorentz)

class FourVector:

    def __init__(self, fourvec, frame: Frame):
    # fourvec is the 4x1 numbers describing the FourVector in the Frame that we are working in. labvec is our FourVector in the lab frame, but is lazy.
        self.fourvec = fourvec.T
        self.frame = frame
        self.labvec = None

    def get_labvec(self):
        if self.labvec is None:
            inverse_lorentz = np.linalg.inv(self.frame.lab_lorentz)
            self.labvec = inverse_lorentz.dot(self.fourvec)
        return self.labvec

    def change_frame(self, newframe):
        self.fourvec = (newframe.lab_lorentz).dot(self.get_labvec())
        self.frame = newframe

    def inner_product(self, X):
        if not self.frame.equals(X.frame):
            raise ValueError("2 FourVector s are not in the same frame")
        return (self.fourvec.T).dot(minkowski_metric).dot(X.fourvec)

    def separation(self, X):
        if self.inner_product(X) < 0:
            return "Timelike"
        elif self.inner_product(X) == 0:
            return "Lightlike"
        else:
            return "Spacelike"

    def add(self, X):
        if not self.frame.equals(X.frame):
            raise ValueError("2 FourVector s are not in the same frame")
        


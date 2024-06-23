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


        


from objects.frames import *
from objects.fourvectors import *

# We will create 2 events event1 and event2
# These will be simultanous in the rest frame 
# However as we will see, if we create a new frame
# which is boosted from the rest frame at 0.5 c in the x direction
# then they are no longer simultanous in this frame
# However, their inner product is consistent, as is their separation

lab_frame = Frame(np.identity(4))
event1 = FourVector(np.array([1,0,0,0]), lab_frame)
event2 = FourVector(np.array([1,1,0,0]), lab_frame)
print("Event 1 and 2 in lab frame:")
print("event1 happens at   " + str(event1.fourvec))
print("event2 happens at   " + str(event2.fourvec))
print("inner product is   " + str(event1.inner_product(event2)))
boosted_frame = lab_frame.boost_x(0.5)
event1.change_frame(boosted_frame)
event2.change_frame(boosted_frame)
print("Event 1 and 2 in boosted frame:")
print("event1 happens at   " + str(event1.fourvec))
print("event2 happens at   " + str(event2.fourvec))
print("inner product is   " + str(event1.inner_product(event2)))


#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import necessary packages
import math
import numpy as np

# gravitational constant
G = 6.674e-11

# masses of each body
m_earth = 5.972e24
m_moon = 7.346e22
m_sun = 1.98892e30
m_jupiter = 1.8986e27
m_saturn = 5.6846e26
m_uranus = 8.6810e25
m_neptune = 1.0243e26
m_pluto = 1.3090e22

# radii of each body
r_earth = 6.371e6
r_moon = 1.737e6
r_sun = 6.96e8
r_jupiter = 6.9911e7
r_saturn = 5.8232e7
r_uranus = 2.5559e7
r_neptune = 2.4764e7
r_pluto = 1.1889e6

# angular momentum of each body
L_earth = 2.0e34
L_moon = 2.7e33
L_sun = 2.86e41
L_jupiter = 1.2e41
L_saturn = 4.2e40
L_uranus = 7.3e39
L_neptune = 5.5e39
L_pluto = 2.6e38

# calculate the effective gravitational potential of the system
V_eff = G*(m_earth/r_earth + m_moon/r_moon + m_sun/r_sun + m_jupiter/r_jupiter + m_saturn/r_saturn + m_uranus/r_uranus + m_neptune/r_neptune + m_pluto/r_pluto) 

# calculate the Lagrange points for the system
L1 = V_eff + G*(m_earth*L_earth**2/(2*r_earth**3) + m_moon*L_moon**2/(2*r_moon**3) + m_sun*L_sun**2/(2*r_sun**3) + m_jupiter*L_jupiter**2/(2*r_jupiter**3) + m_saturn*L_saturn**2/(2*r_saturn**3) + m_uranus*L_uranus**2/(2*r_uranus**3) + m_neptune*L_neptune**2/(2*r_neptune**3) + m_pluto*L_pluto**2/(2*r_pluto**3))

L2 = V_eff - G*(m_earth*L_earth**2/(2*r_earth**3) + m_moon*L_moon**2/(2*r_moon**3) + m_sun*L_sun**2/(2*r_sun**3) + m_jupiter*L_jupiter**2/(2*r_jupiter**3) + m_saturn*L_saturn**2/(2*r_saturn**3) + m_uranus*L_uranus**2/(2*r_uranus**3) + m_neptune*L_neptune**2/(2*r_neptune**3) + m_pluto*L_pluto**2/(2*r_pluto**3))

# print the results
print("The effective gravitational potential of the system is:", V_eff)
print("The Lagrange points for the system are: L1 =", L1, "and L2 =", L2)


# In[ ]:





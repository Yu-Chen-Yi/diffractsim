import diffractsim
diffractsim.set_backend("CUDA") #Change the string to "CUDA" to use GPU acceleration

from diffractsim import MonochromaticField, nm, mm, cm, RectangularSlit

F = MonochromaticField(
    wavelength = 632.8 * nm, extent_x=78. * mm, extent_y=78. * mm, Nx=4096, Ny=4096, intensity =0.01
)

def L_letter(cx,cy,L):
    return RectangularSlit(width = 0.2*L, height = 1.0*L, x0 = cx-L/2*0.8 , y0 = cy) + RectangularSlit(width = 0.8*L, height = 0.2*L, x0 = cx+0.1*L, y0 = cy-L/2*0.8)

def F_letter(cx,cy,L):
    return RectangularSlit(width = 0.2*L, height = 1.0*L, x0 = cx-L/2*0.8 , y0 = cy) + RectangularSlit(width = 0.8*L, height = 0.2*L, x0 = cx+0.1*L, y0 = cy+L/2*0.8) + RectangularSlit(width = 0.6*L, height = 0.2*L, x0 = cx-0*L, y0 = cy+L/2*0.1)

def rect4(cx,cy,L,D):
    return RectangularSlit(width = 0.2*L, height = 0.2*L, x0 = cx-D , y0 = cy+D) + RectangularSlit(width = 0.7*L, height = 0.7*L, x0 = cx+D, y0 = cy+D) + RectangularSlit(width = 0.45*L, height = 0.45*L, x0 = cx+D, y0 = cy-D) + RectangularSlit(width = 1*L, height = 1*L, x0 = cx-D, y0 = cy-D)

L = 0.6*mm
Dx = 2 * mm
Dy = 2 * mm
mask = rect4(0,0,0,0)
for i in range(-20,21):
    for j in range(-10,11):
        cx = Dx*i
        cy = Dy*j
        mask = mask + rect4(cx,cy,L,Dx/4)
F.add(mask)


# plot the double slit
rgb = F.get_colors()
F.plot_colors(rgb, xlim=[-4* mm, 4* mm], ylim=[-4* mm, 4* mm]) 

 
z = 1/2*Dx**2/(632.8*nm)
# propagate the field and scale the viewing extent four times: (new_extent_x = old_extent_x * 4 = 80* mm)
#F.scale_propagate(400*cm, scale_factor = 4)
F.zoom_propagate(z, x_interval = [-4 * mm, 4 * mm], y_interval = [-4 * mm, 4 * mm])



# plot the double slit diffraction pattern colors
rgb = F.get_colors()
F.plot_colors(rgb) 

# plot the intensity
I = F.get_intensity()
F.plot_intensity(I, square_root = True, units = mm, grid = True, figsize = (14,5), slice_y_pos = 0*mm)
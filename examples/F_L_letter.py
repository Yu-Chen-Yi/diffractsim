import diffractsim
diffractsim.set_backend("CUDA") #Change the string to "CUDA" to use GPU acceleration

from diffractsim import MonochromaticField, nm, mm, cm, RectangularSlit

F = MonochromaticField(
    wavelength = 632.8 * nm, extent_x=78. * mm, extent_y=78. * mm, Nx=2048, Ny=2048, intensity =0.01
)

def L_letter(cx,cy,L):
    return RectangularSlit(width = 0.2*L, height = 1.0*L, x0 = cx-L/2*0.8 , y0 = cy) + RectangularSlit(width = 0.8*L, height = 0.2*L, x0 = cx+0.1*L, y0 = cy-L/2*0.8)

def F_letter(cx,cy,L):
    return RectangularSlit(width = 0.2*L, height = 1.0*L, x0 = cx-L/2*0.8 , y0 = cy) + RectangularSlit(width = 0.8*L, height = 0.2*L, x0 = cx+0.1*L, y0 = cy+L/2*0.8) + RectangularSlit(width = 0.6*L, height = 0.2*L, x0 = cx-0*L, y0 = cy+L/2*0.1)

L = 1*mm
Dx = 2 * mm
Dy = 2 * mm
mask = L_letter(0,0,0)
for i in range(-10,11):
    for j in range(-10,11):
        cx = Dx*i
        cy = Dy*j
        if j%2 == 1:
            mask = mask + F_letter(cx,cy,L)
        else:
            mask = mask + L_letter(cx,cy,L)
F.add(mask)


# plot the double slit
rgb = F.get_colors()
F.plot_colors(rgb, xlim=[-9* mm, 9* mm], ylim=[-9* mm, 9* mm]) 

 
z = 2*Dx**2/(632.8*nm)
# propagate the field and scale the viewing extent four times: (new_extent_x = old_extent_x * 4 = 80* mm)
#F.scale_propagate(400*cm, scale_factor = 4)
F.zoom_propagate(z, x_interval = [-9 * mm, 9 * mm], y_interval = [-9 * mm, 9 * mm])



# plot the double slit diffraction pattern colors
rgb = F.get_colors()
F.plot_colors(rgb) 

# plot the intensity
I = F.get_intensity()
F.plot_intensity(I, square_root = True, units = mm, grid = True, figsize = (14,5), slice_y_pos = 0*mm)
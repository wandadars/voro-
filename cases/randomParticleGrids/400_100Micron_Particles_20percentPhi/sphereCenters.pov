#version 3.6;

// Right-handed coordinate system in which the z-axis points upwards
camera {
	location <-0.002,0.0016,0.0016>
	direction 1.0*z
	right x
	up y
	look_at <0,0,0>
}

// White background
background{rgb 1}

// Two lights with slightly different colors
light_source{<-8,-20,30> color rgb <0.77,0.75,0.75>}
light_source{<25,-12,12> color rgb <0.38,0.40,0.40>}

// Radius of the Voronoi cell network
#declare r=0.00001;

// Radius of the particles
#declare s=0.00005;

// Particles
union{
#include "sphereCenters_p.pov"
	pigment{rgb 0.95} finish{reflection 0.1 specular 0.3 ambient 0.42}
}

// Voronoi cells
union{
#include "sphereCenters_v.pov"
	pigment{rgb <1,0.4,0.45>} finish{specular 0.5 ambient 0.42}
}

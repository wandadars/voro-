// File import example code
//
// Author   : Chris H. Rycroft (LBL / UC Berkeley)
// Email    : chr@alum.mit.edu
// Date     : August 30th 2011

#include "voro++.hh"
using namespace voro;

// Set up constants for the container geometry
const double x_min=-0.000870616,x_max=0.000870616;
const double y_min=-0.0004,y_max=0.0004;
const double z_min=-0.0004,z_max=0.0004;

// Set up the number of blocks that the container is divided into
const int n_x=6,n_y=3,n_z=3;

int main() {

	// Create a container with the geometry given above, and make it
	// non-periodic in each of the three coordinates. Allocate space for
	// eight particles within each computational block
	container_poly conp(x_min,x_max,y_min,y_max,z_min,z_max,n_x,n_y,n_z,
			false,false,false,20);

	//Randomly add particles into the container
	conp.import("sphereCenters.inp");

	// Save the Voronoi network of all the particles to text files
	// in gnuplot and POV-Ray formats
	conp.draw_cells_gnuplot("sphereCenters.gnu");
	conp.draw_cells_pov("sphereCenters_v.pov");

	// Output the particles in POV-Ray format
	conp.draw_particles_pov("sphereCenters_p.pov");



	// Do a custom output routine that outputs the particle IDs and
	// positions, plus the volume and the centroid position relative to the
	// particle center
	conp.print_custom("%i %q %r %s %v %C","VoronoiData.dat");

	
	// Export the normal vectors of each face of the voronoi cell for each particle
	conp.print_custom("%i %q %l","VoronoiFaceVectors.dat");



}

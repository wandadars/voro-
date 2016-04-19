##############################################################################
#               Makefile.am
#
# Process this file with automake to produce Makefile.in
#
# ---------------------------------------------------------------------------
# Persistence of Vision Ray Tracer ('POV-Ray') version 3.7.
# Copyright 1991-2013 Persistence of Vision Raytracer Pty. Ltd.
#
# POV-Ray is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# POV-Ray is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ---------------------------------------------------------------------------
# POV-Ray is based on the popular DKB raytracer version 2.12.
# DKBTrace was originally written by David K. Buck.
# DKBTrace Ver 2.0-2.12 were written by David K. Buck & Aaron A. Collins.
##############################################################################

# Makefile.am for the source distribution of POV-Ray 3.7 for UNIX
# Written by POV-Ray Bugtracker http://bugs.povray.org/

# Libraries to build.
noinst_LIBRARIES = libpovray.a

# Source files.
libpovray_a_SOURCES = \
optout.cpp pov_mem.cpp precomp.cpp pov_mem.h backend/math/quatern.h backend/math/hcmplx.cpp backend/math/chi2.cpp backend/math/hcmplx.h backend/math/polysolv.h backend/math/quatern.cpp backend/math/splines.cpp backend/math/splines.h backend/math/mathutil.h backend/math/matrices.h backend/math/polysolv.cpp backend/math/chi2.h backend/math/matrices.cpp backend/math/vector.h backend/math/mathutil.cpp backend/lighting/photons.cpp backend/lighting/point.h backend/lighting/photonstrategytask.cpp backend/lighting/photonshootingstrategy.cpp backend/lighting/subsurface.cpp backend/lighting/photonestimationtask.h backend/lighting/radiosity.h backend/lighting/photonshootingtask.h backend/lighting/photonstrategytask.h backend/lighting/radiosity.cpp backend/lighting/photonestimationtask.cpp backend/lighting/photonshootingtask.cpp backend/lighting/photonsortingtask.h backend/lighting/photonsortingtask.cpp backend/lighting/point.cpp backend/lighting/photons.h backend/lighting/subsurface.h backend/lighting/rad_data.cpp backend/lighting/photonshootingstrategy.h backend/pattern/pattern.cpp backend/pattern/pattern.h backend/pattern/warps.cpp backend/pattern/warps.h backend/scene/atmosph.cpp backend/scene/camera.cpp backend/scene/threaddata.cpp backend/scene/threaddata.h backend/scene/atmosph.h backend/scene/objects.cpp backend/scene/objects.h backend/scene/scene.cpp backend/scene/scene.h backend/scene/camera.h backend/scene/view.cpp backend/scene/view.h backend/povray.h backend/render/rendertask.h backend/render/ray.cpp backend/render/radiositytask.cpp backend/render/radiositytask.h backend/render/tracetask.cpp backend/render/trace.cpp backend/render/rendertask.cpp backend/render/tracepixel.cpp backend/render/ray.h backend/render/tracetask.h backend/render/tracepixel.h backend/render/trace.h backend/texture/pigment.cpp backend/texture/avxfma4check.h backend/texture/normal.h backend/texture/pigment.h backend/texture/texture.cpp backend/texture/texture.h backend/texture/normal.cpp backend/control/renderbackend.h backend/control/benchmark.h backend/control/messagefactory.cpp backend/control/renderbackend.cpp backend/control/messagefactory.h backend/control/benchmark.cpp backend/shape/blob.h backend/shape/truetype.h backend/shape/polygon.h backend/shape/spheres.cpp backend/shape/csg.cpp backend/shape/sor.h backend/shape/isosurf.h backend/shape/fractal.cpp backend/shape/triangle.h backend/shape/torus.cpp backend/shape/isosurf.cpp backend/shape/mesh.h backend/shape/cones.cpp backend/shape/lathe.h backend/shape/cones.h backend/shape/bezier.cpp backend/shape/boxes.cpp backend/shape/ovus.h backend/shape/discs.h backend/shape/fractal.h backend/shape/csg.h backend/shape/planes.h backend/shape/spheres.h backend/shape/torus.h backend/shape/mesh.cpp backend/shape/hfield.h backend/shape/fpmetric.h backend/shape/boxes.h backend/shape/planes.cpp backend/shape/blob.cpp backend/shape/sphsweep.h backend/shape/ovus.cpp backend/shape/prism.h backend/shape/prism.cpp backend/shape/polygon.cpp backend/shape/hfield.cpp backend/shape/triangle.cpp backend/shape/poly.h backend/shape/truetype.cpp backend/shape/quadrics.h backend/shape/bezier.h backend/shape/super.cpp backend/shape/fpmetric.cpp backend/shape/poly.cpp backend/shape/super.h backend/shape/sphsweep.cpp backend/shape/sor.cpp backend/shape/discs.cpp backend/shape/quadrics.cpp backend/shape/lathe.cpp backend/bounding/bbox.h backend/bounding/bsphere.cpp backend/bounding/bbox.cpp backend/bounding/bsphere.h backend/bounding/boundingtask.cpp backend/bounding/bcyl.h backend/bounding/bcyl.cpp backend/bounding/boundingtask.h backend/frame.h backend/parser/tokenize.cpp backend/parser/parsestr.cpp backend/parser/parse.h backend/parser/function.cpp backend/parser/reswords.cpp backend/parser/reswords.h backend/parser/fnsyntax.cpp backend/parser/parstxtr.cpp backend/parser/parse.cpp backend/parser/express.cpp backend/vm/fnintern.cpp backend/vm/fncode.cpp backend/vm/fncode.h backend/vm/fnpovfpu.cpp backend/vm/fnintern.h backend/vm/fnpovfpu.h backend/colour/colutils.h backend/colour/spectral.h backend/colour/colour.h backend/colour/spectral.cpp backend/colour/colutils.cpp backend/colour/colour.cpp backend/support/randomsequences.h backend/support/statistics.cpp backend/support/fileutil.h backend/support/fixedallocator.h backend/support/octree.h backend/support/taskqueue.cpp backend/support/msgutil.cpp backend/support/simplevector.h backend/support/task.h backend/support/msgutil.h backend/support/fileutil.cpp backend/support/bsptree.h backend/support/imageutil.cpp backend/support/jitter.h backend/support/taskqueue.h backend/support/randomsequences.cpp backend/support/statistics.h backend/support/jitter.cpp backend/support/bsptree.cpp backend/support/imageutil.h backend/support/octree.cpp backend/support/task.cpp backend/interior/media.h backend/interior/media.cpp backend/interior/interior.h backend/interior/interior.cpp backend/povray.cpp backend/configbackend.h precomp.h lightgrp.h povrayold.h frontend/shelloutprocessing.h frontend/console.cpp frontend/imagemessagehandler.cpp frontend/animationprocessing.h frontend/imageprocessing.cpp frontend/processrenderoptions.cpp frontend/filemessagehandler.h frontend/rendermessagehandler.h frontend/console.h frontend/parsermessagehandler.h frontend/display.h frontend/imageprocessing.h frontend/configfrontend.h frontend/processrenderoptions.h frontend/animationprocessing.cpp frontend/shelloutprocessing.cpp frontend/defaultplatformbase.h frontend/renderfrontend.cpp frontend/filemessagehandler.cpp frontend/parsermessagehandler.cpp frontend/renderfrontend.h frontend/rendermessagehandler.cpp frontend/imagemessagehandler.h frontend/defaultplatformbase.cpp frontend/display.cpp frontend/simplefrontend.h lightgrp.cpp base/path.cpp base/textstreambuffer.h base/safemath.h base/textstream.cpp base/povms.cpp base/fileinputoutput.cpp base/timer.cpp base/textstream.h base/timer.h base/image/png_pov.h base/image/colourspace.h base/image/iff.cpp base/image/image.cpp base/image/iff.h base/image/metadata.h base/image/ppm.cpp base/image/jpeg_pov.h base/image/bmp.h base/image/gifdecod.cpp base/image/openexr.cpp base/image/png.cpp base/image/hdr.h base/image/jpeg.cpp base/image/openexr.h base/image/encoding.cpp base/image/pgm.h base/image/bmp.cpp base/image/encoding.h base/image/tiff_pov.h base/image/ppm.h base/image/gif.h base/image/targa.cpp base/image/hdr.cpp base/image/gif.cpp base/image/image.h base/image/colourspace.cpp base/image/targa.h base/image/pgm.cpp base/image/tiff.cpp base/pov_err.h base/platformbase.h base/fileinputoutput.h base/povmscpp.cpp base/configbase.h base/textstreambuffer.cpp base/pointer.h base/types.h base/processoptions.cpp base/path.h base/povmsgid.h base/stringutilities.cpp base/povdebug.h base/processoptions.h base/povms.h base/font/timrom.h base/font/timrom.cpp base/font/crystal.cpp base/font/povlogo.cpp base/font/povlogo.h base/font/cyrvetic.h base/font/cyrvetic.cpp base/font/crystal.h base/animation/moov.cpp base/animation/moov.h base/animation/animation.h base/animation/animation.cpp base/povmscpp.h base/pov_err.cpp base/stringutilities.h statspov.h

# Include paths for headers.
AM_CPPFLAGS = \
  -I$(top_srcdir) \
  -I$(top_srcdir)/source/backend \
  -I$(top_srcdir)/source/base \
  -I$(top_srcdir)/source/frontend \
  -I$(top_srcdir)/unix \
  -I$(top_srcdir)/vfe \
  -I$(top_srcdir)/vfe/unix

# Video Avatars

This repository contains code corresponding to the paper **Video based reconstruction of 3D people models**.

updated 

## Installation

Download and unpack the SMPL model from here: http://smpl.is.tue.mpg.de/.
also SMPLX https://smpl-x.is.tue.mpg.de/    and model correspondences

Download and unpack the SMPLify Code from here: http://smplify.is.tue.mpg.de/

make sure CUDA is installed on your machine > 10.1

```
git clone https://github.com/thmoa/videoavatars.git
cd videoavatars/vendor
mkdir smpl
cd smpl
ln -s <path to smpl folder>/models .
ln -s <path to smpl folder>/smpl_webuser/*.py .
cd ..

mkdir smplx
ln -s <path to smplx folder>/models/smplx .

mkdir smplify
cd smplify
touch __init__.py
ln -s <path to your smplify installation>/code/models .
# this file needs to be copied!
cp <path to your smplify installation>/code/lib/sphere_collisions.py .
# these files can be linked
ln -s <path to smplify folder>/code/lib/capsule_body.py .
ln -s <path to smplify folder>/code/lib/capsule_ch.py .
ln -s <path to smplify folder>/code/lib/robustifiers.py .

cd ..

conda env create -f environment.yaml
pip install --upgrade pip
git clone https://github.com/polmorenoc/opendr.git
cd opendr/opendr
python ./setup.py install

cd ../..
```

Change line 14 in `vendor/smplify/sphere_collisions.py` to
```
from vendor.smpl.lbs import verts_core
```

## Usage

The software consists of three parts:

1. `step1_pose.py`: pose reconstruction
2. `step2_consensus.py`: consensus shape optimization
3. `step3_texture.py`: texture calculation

Starting the scripts will display usage information and options.
Additionally, we provide helper bash scripts for easier processing of our dataset.

The scripts in `prepare_data` might help you to process your own data.

usage:

1. run openpose on data   `.\bin\OpenPoseDemo.exe --image_dir .\sasmit_images\ --write_json .\keypoints1 --display 0 --render_pose 0 --model_pose COCO`
2. `python .\prepare_data\2djoints2hdf5.py data\keypoints keypoints.hdf5`
3. create masks on data (im using segment anything)
4. `python .\prepare_data\masks2hdf5.py .\data\mask\ masks.hdf5`
5. `python .\prepare_data\create_camera.py camera.pkl 1080 1920 -f 900.0 900.0`
6. `python .\step1_pose.py .\keypoints.hdf5 .\masks.hdf5 .\camera.pkl step1`

## Citation

This repository contains code corresponding to:

T. Alldieck, M. Magnor, W. Xu, C. Theobalt, and G. Pons-
Moll. **Video based reconstruction of 3D people models**. In
*IEEE Conference on Computer Vision and Pattern Recognition*, 2018.

Please cite as:

```
@inproceedings{alldieck2018video,
  title = {Video Based Reconstruction of 3D People Models},
  author = {Alldieck, Thiemo and Magnor, Marcus and Xu, Weipeng and Theobalt, Christian and Pons-Moll, Gerard},
  booktitle = {{IEEE} Conference on Computer Vision and Pattern Recognition},
  year = {2018}
}
```


## Dataset

The accompanied dataset can be downloaded here: https://graphics.tu-bs.de/people-snapshot

## License

Copyright (c) 2018 Thiemo Alldieck, Technische Universität Braunschweig, Max-Planck-Gesellschaft

**Please read carefully the following terms and conditions and any accompanying documentation before you download and/or use this software and associated documentation files (the "Software").**

The authors hereby grant you a non-exclusive, non-transferable, free of charge right to copy, modify, merge, publish, distribute, and sublicense the Software for the sole purpose of performing non-commercial scientific research, non-commercial education, or non-commercial artistic projects.

Any other use, in particular any use for commercial purposes, is prohibited. This includes, without limitation, incorporation in a commercial product, use in a commercial service, or production of other artefacts for commercial purposes.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

You understand and agree that the authors are under no obligation to provide either maintenance services, update services, notices of latent defects, or corrections of defects with regard to the Software. The authors nevertheless reserve the right to update, modify, or discontinue the Software at any time.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. You agree to cite the **Video Based Reconstruction of 3D People Models** paper in documents and papers that report on research using this Software.

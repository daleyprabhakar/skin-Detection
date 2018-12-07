# Skin Detection
Skin detection is the process of finding skin-colored pixels and regions in an image or a video.
This process is typically used as a preprocessing step to find regions that potentially have human
faces and limbs in images. Several computer vision approaches have been developed for skin
detection. A skin detector typically transforms a given pixel into an appropriate color space and
then use a skin classifier to label the pixel whether it is a skin or a non-skin pixel. A skin classifier
defines a decision boundary of the skin color class in the color space based on a training database
of skin-colored pixels.

Skin color and textures are important cues that people use consciously or unconsciously to infer
variety of culture-related aspects about each other. Skin color and texture can be an indication of
race, health, age, wealth, beauty, etc. However, such interpretations vary across cultures and
across the history. In images and videos, skin color is an indication of the existence of humans in
such media. Therefore, in the last two decades extensive research have focused on skin detection
in images. Skin detection means detecting image pixels and regions that contain skin-tone color.
Most the research in this area have focused on detecting skin pixels and regions based on their
color. Very few approaches attempt to also use texture information to classify skin pixels.
As will be described shortly, detecting skin pixels are rather computationally easy task and
can be done very efficiently, a feature that encourages the use of skin detection in many video
analysis applications. For example, in one of the early applications, detecting anchors in TV news 
videos for the sake of video automatic annotation, archival, and retrieval. In such an application, 
it is typical that the face and the hands of the anchor person are the largest skin-tone colored region 
in a given frame since, typically, news programs are shot in indoor controlled environments with man-made
background materials that hardly contain skin-colored objects. In many similar applications, where
the background is controlled or unlikely to contain skin-colored regions, detecting skin-colored
pixels can be a very efficient cue to find human faces and hands in images. An example in the
context of biometric is detecting faces for face recognition in an controlled environment.

Detecting skin-colored pixels, although seems a straightforward easy task, has proven quite
challenging for many reasons. The appearance of skin in an image depends on the illumination
conditions (illumination geometry and color) where the image was captured. We humans are very
good at identifying object colors in a wide range of illuminations, this is called color constancy.
Color constancy is a mystery of perception. Therefore, an important challenge in skin detection is
to represent the color in a way that is invariant or at least insensitive to changes in illumination. As
will be discussed shortly, the choice of the color space affects greatly the performance of any skin
detector and its sensitivity to change in illumination conditions. Another challenge comes from the
fact that many objects in the real world might have skin-tone colors. For example, wood, leather,
skin-colored clothing, hair, sand, etc. This causes any skin detector to have many false detections
in the background if the environment is not controlled.

<p align="center">
  <img src="data/Capture.png"  width=544 height=613>
</p>

# Framework for Skin Detection: 

Skin detection process has two phases: a training phase and a detection phase. Training a skin
detector involves three basic steps:
1.  Collecting a database of skin patches from different images. Such a database typically contains
    skin-colored patches from a variety of people under different illumination conditions.
    (Data collected from random Google Search)
2.  Choosing a suitable color space.
3.  Learning the parameters of a skin classifier.

Given a trained skin detector, identifying skin pixels in a given image or video frame involves:
1.  Converting the image into the same color space that was used in the training phase.
2.  Classifying each pixel using the skin classifier to either a skin or non-skin.
3.  Typically post processing is needed using morphology to impose spatial homogeneity on the
    detected regions.
    
In any given color space, skin color occupies a part of such a space, which might be a compact
or large region in the space. Such region is usually called the skin color cluster. A skin classifier is
a one-class or two-class classification problem. A given pixel is classified and labeled whether it
is a skin or a non-skin given a model of the skin color cluster in a given color space. In the context
of skin classification, true positives are skin pixels that the classifier correctly labels as skin. True
negatives are non-skin pixels that the classifier correctly labels as non-skin. Any classifier makes
errors: it can wrongly label a non-skin pixel as skin or a skin pixel as a non-skin. The former type
of errors is referred to as false positives (false detections) while the later is false negatives. A good
classifier should have low false positive and false negative rates. As in any classification problem,
there is a tradeoff between false positives and false negatives. The more loose the class boundary,
the less the false negatives and the more the false positives. The tighter the class boundary, the
more the false negatives and the less the false positives. The same applies to skin detection. This
makes the choice of the color space extremely important in skin detection. The color needs to
be represented in a color space where the skin class is most compact in order to be able to tightly
model the skin class. The choice of the color space directly affects the kind of classifier that should
be used.

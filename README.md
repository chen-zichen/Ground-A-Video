# Ground-A-Video: Zero-shot Grounded Video Editing using Text-to-image Diffusion Models

This repository contains the official pytorch implementation of [Ground-A-Video](#).
<br/> <br/>
[![Project Website](https://img.shields.io/badge/Project-Website-orange)](https://ground-a-video.github.io/)

## 🌱 Abstract
<b><font color="red">Ground A Video</font> is the first groundings-driven video editing.<br>
<font color="red">Ground A Video</font> is the first video editing framework that integrates spatially-continuous and spatially-discrete conditions.<br>
<font color="red">Ground A Video</font> does not neglect edits, confuse edits, but does preserve non-target regions.<br>
:o: Pretrained Stable Diffusion |
:o: Optical Flow, Depth Map, Groundings |
:x: Any training</b>

<details><summary>Full abstract</summary>


> We introduce a novel groundings guided video-to-video translation framework called Ground-A-Video. Recent endeavors in video editing have showcased promising results in single-attribute editing or style transfer tasks, either by training T2V models on text-video data or adopting training-free methods. However, when confronted with the complexities of multi-attribute editing scenarios, they exhibit shortcomings such as omitting or overlooking intended attribute changes, modifying the wrong elements of the input video, and failing to preserve regions of the input video that should remain intact. Ground-A-Video attains temporally consistent multi-attribute editing of input videos in a training-free manner without aforementioned shortcomings. Central to our method is the introduction of cross-frame gated attention which incorporates groundings information into the latent representations in a temporally consistent fashion, along with Modulated Cross-Attention and optical flow guided inverted latents smoothing. Extensive experiments and applications demonstrate that Ground-A-Video's zero-shot capacity outperforms other baseline methods in terms of edit-accuracy and frame consistency.
</details>

## Teaser
<table class="center">
<tr>
  <td style="text-align:center;"><b>Input Video</b></td>
  <td style="text-align:center;"><b>Video Groundings</b></td>
  <td style="text-align:center;"><b>Depth Map</b></td>
  <td style="text-align:center;"><b>Optical Flow</b></td>
  <td style="text-align:center;"><b>Output Video</b></td>
</tr>

<tr>
  <td width=20% style="text-align:center;color:gray;">"A man is walking a dog on the road."</td>
  <td width=20% style="text-align:center;"><b style='color:blue;'>man</b>, <b style='color:red;'>dog</b>, <b style='color:orange;'>road</b></td>
  <td width=20% style="text-align:center;color:gray;">by ZoeDepth</td>
  <td width=20% style="text-align:center;">by RAFT-large</td>
  <td width=20% style="text-align:center;color:gray;">"Iron Man is walking a sheep on the lake."</td>
</tr>

<tr>
  <td style colspan="1"><img src="assets/dog_walking/input.gif"></td>
  <td style colspan="1"><img src="assets/dog_walking/grounding.gif"></td>
  <td style colspan="1"><img src="assets/dog_walking/depth.gif"></td>  
  <td style colspan="1"><img src="assets/dog_walking/flow.gif"></td> 
  <td style colspan="1"><img src="assets/dog_walking/output.gif"></td>  
</tr>

<tr>
  <td style="text-align:center;"><b>Input Video</b></td>
  <td style="text-align:center;"><b>Video Groundings</b></td>
  <td style="text-align:center;"><b>Depth Map</b></td>
  <td style="text-align:center;"><b>Optical Flow</b></td>
  <td style="text-align:center;"><b>Output Video</b></td>
</tr>

<tr>
  <td width=20% style="text-align:center;color:gray;">"A rabbit is eating a watermelon on the table."</td>
  <td width=20% style="text-align:center;"><b style='color:red;'>rabbit</b>, <b style='color:blue;'>watermelon</b>, <b style='color:purple;'>table</b></td>
  <td width=20% style="text-align:center;color:gray;">by ZoeDepth</td>
  <td width=20% style="text-align:center;">by RAFT-large</td>
  <td width=20% style="text-align:center;color:gray;">"A squirrel is eating an orange on the grass, under the aurora."</td>
</tr>

<tr>
  <td style colspan="1"><img src="assets/rabbit_watermelon/input.gif"></td>
  <td style colspan="1"><img src="assets/rabbit_watermelon/grounding.gif"></td>
  <td style colspan="1"><img src="assets/rabbit_watermelon/depth.gif"></td>  
  <td style colspan="1"><img src="assets/rabbit_watermelon/flow.gif"></td> 
  <td style colspan="1"><img src="assets/rabbit_watermelon/output.gif"></td>  
</tr>

</table>


## Code, Data, Environment

<strong style="color:darkblue;">Coming soon !</strong>

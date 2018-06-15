# Adversarial Machine Learning Paper

Papers about **[Adversarial Machine Learning](https://en.wikipedia.org/wiki/Adversarial_machine_learning)**.

( **Not** to be confused with Generative adversarial network, GAN )

## The FIRST Paper

In this paper, the author first noticed the existence of *adversarial examples* in image classification application.

* **L-BFGS**Intriguing properities of neural networkds,2013 , [ [paper](https://arxiv.org/abs/1312.6199) ] 

## Introduction and Analysis

*  Adversarial Machine Learning, 2011,  [ [paper](https://people.eecs.berkeley.edu/~tygar/papers/SML2/Adversarial_AISEC.pdf) ] 
*  Adversarial examples in the physical world 
* Exploring the space of adversarial images
* Analysis of classifiers’ robustness to adversarial perturbations
* Adversarial Examples Are Not Easily Detected: Bypassing Ten Detection Methods, Nicholas Carlini & David Wagner, [ [code](https://github.com/abhibhav14/adversarial-attacks-papernotes/blob/master/notes/carlini-wagner-bypass.md) ], [[paper](https://arxiv.org/abs/1705.07263)]
* Analysis of classifiers' robustness to adversarial perturbations, Machine Learning , [  [paper](https://link.springer.com/article/10.1007%2Fs10994-017-5663-3)]
* Adversarial Machine Learning at Scale, **ICLR 2017**,[ [paper](https://openreview.net/forum?id=BJm4T4Kgx) ] 
* ADVERSARIAL EXAMPLES FOR GENERATIVE MODELS
* Transferability in Machine Learning: from Phenomena to Black-Box Attacks using Adversarial Samples
* The Space of Transferable Adversarial Examples
* Adversarial Examples that Fool both Human and Computer Vision 


## Survey

* Adversarial Examples: Attacks and Defenses for Deep Learning, 2018, [ [paper](https://arxiv.org/abs/1712.07107)  ], 
* Towards the Science of Security and Privacy in Machine Learning, Patrick McDaniel [cyw to read]
* Threat of Adversarial Attacks on Deep Learning in Computer Vision: A Survey ,  , 2018 ,CoRR, [ [paper](https://arxiv.org/abs/1801.00553) ]

## Attacks

In this category, the author usually luanch an attack to an classifier model, trained using CNN or other machine learning algorithms. A typical way to attack is to add some kind of small **noise** directly to the matrix (or image) and feed it into the target classifier, then get a different (false) classification result.

* **FGSM** : Explaining and Harnessing Adversarial Examples 
* **RAND + FGSM** : Practical Black-Box Attacks against Machine Learning 
* **CW-Attack** : Towards Evaluating the Robustness of Neural Networks, Nicholas Carlini & David Wagner, [  [paper](https://arxiv.org/abs/1608.04644) ]
* **Traffic Light** : Fooling Vision and Language Models Despite Localization and Attention Mechanism , **CVPR 2018**
* **Hack ICLR 2018** : Obfuscated Gradients Give a False Sense of Security : Circumventing Defenses to Adversarial Examples
* Deep neural networks are easily fooled: High confidence predictions for unrecognizable images
* Targeted Backdoor Attacks on Deep Learning Systems Using Data Poisoning, Chang Liu, [  [paper](https://arxiv.org/abs/1712.05526) ]
* Manipulating Machine Learning: Poisoning Attacks and Countermeasures for Regression Learning , **Oakland '18** ,Chang Liu, [  [paper](https://arxiv.org/pdf/1804.00308.pdf) ]
* Robust Linear Regression Against Training Data Poisoning, **AISec@CCS 17** , [ [paper](https://people.eecs.berkeley.edu/~liuchang/paper/aisec17-poisoning.pdf) ]
* Delving into Transferable Adversarial Examples and Black-box Attacks, **ICLR '17**,  [  [paper](https://arxiv.org/abs/1611.02770) ]
* Shielding Google's language toxicity model against adversarial attacks  , [ [paper](https://arxiv.org/abs/1801.01828) ]
* Generating Adversarial Examples with Adversarial Networks, **Dawn Song**, [ [paper](https://arxiv.org/abs/1801.02610) ]
* Spatially Transformed Adversarial Examples, **Dawn Song**, [ [paper](https://arxiv.org/abs/1801.02612)]
* Adversarial Deep Learning for Robust Detection of Binary Encoded Malware, [ [paper](https://arxiv.org/abs/1801.02950) ] 
* **Black box Attack** : Black-box Generation of Adversarial Text Sequences to Evade Deep Learning Classifiers, [ [paper](https://arxiv.org/abs/1801.04354)]



###  Attacks to Face or Speech Recognition

In this category, the attacker focus on a face recognition system (like Face++), to make the classifier misclassify the input face or cannot detect faces.

* Accessorize to a Crime:Real and Stealthy Attacks on State-of-the-Art Face Recognition
* Invisible Mask: Practical Attacks on Face Recognition with Infrared
* Adversarial Generative Nets: Neural Network Attacks on State-of-the-Art Face Recognition ,   [ [paper](https://arxiv.org/abs/1801.00349) ]
* **Speech** : Did you hear that? Adversarial Examples Against Automatic Speech Recognition,  [ [paper](https://arxiv.org/abs/1801.00554) ]
* High Dimensional Spaces, Deep Learning and Adversarial Examples, [ [paper](https://arxiv.org/abs/1801.00634) ]
* **Speech** : * Audio Adversarial Examples: Targeted Attacks on Speech-to-Text, [ [paper](https://arxiv.org/abs/1801.01953) ] **white box, targeted attack, directed input**
* Adversarial Vulnerability of Neural Networks Increases With Input Dimension , [ [paper](https://arxiv.org/abs/1802.01421) ]


### Attacks to Malware Detection

* Evading Classifiers by Morphing in the Dark, **black-box attack**
* Adversarial examples for malware detection
* Automated poisoning attacks and defenses in malware detection systems: An adversarial machine learning approach, 2018 , **Computers & Security**, [ [paper](https://www.sciencedirect.com/science/article/pii/S0167404817302444?via%3Dihub)]
* Adversarially Robust Malware Detection Using Monotonic Classification,CODASPY 2018, [ [paper](https://dl.acm.org/citation.cfm?doid=3180445.3180449) ]
* Adversarial Training Methods for Semi-Supervised Text Classification , **ICLR 2017**, [ [paper](https://openreview.net/forum?id=r1X3g2_xl) ]



## Defenses

In this category, some defensive techniques are proposed, the way to defense adversarial various and some typical defense method are listed:

- Detecting the adversarial examples
- Increase the robustness of the classifier (especially neural networks)
- Add pre-processing process before feed samples into the classifier
- etc.

Papers:

* Detecting Adversarial Examples in Deep Networks with Adaptive Noise Reduction, detecting, 2018
* SafetyNet: Detecting and Rejecting Adversarial Examples Robustly
* Improving the Robustness of Deep Neural Networks via Stability Training
* Efficient Defenses Against Adversarial Attacks
* Distillation as a Defense to Adversarial Perturbations Against Deep Neural Networks 
* MagNet: a Two-Pronged Defense against Adversarial Examples
* Hardening Deep Neural Networks via Adversarial Model Cascades, [ [paper](https://arxiv.org/abs/1802.01448) ] 
* On Detecting Adversarial Perturbations, **ICLR 2017**, [[paper](https://openreview.net/pdf?id=SJzCSf9xg)]





## Stealing Machine Learning Models

* Cracking Classifiers for Evasion: A Case Study on the Google’s Phishing Pages Filter
* Stealing Machine Learning Models via Prediction APIs, **USENIX 2016**


## Stealing Data


* **Stealing Training Data** : Model Inversion Attacks that Exploit Confidence Information and Basic Countermeasures, [ [paper](https://dl.acm.org/citation.cfm?doid=2810103.2813677) ]
* **Model Inversion Attack** :
* **Use GAN to steal data** : 




## To Added Papers



* **Black box Attack** : Delving into Transferable Adversarial Examples and Black-box Attacks
* **traffic sign** : Robust Physical-World Attacks on Deep Learning Models

* **Speech** : DolphinAttack: Inaudible Voice Commands

* Adversarial Perturbations Against Deep Neural Networks for Malware Classific
* Automatically Evading Classifiers: A Case Study on PDF Malware Classifiers

* Defensive distillation is not robust to adversarial examples
* **R+FGSM**Ensemble Adversarial Training: Attacks and Defenses [ [paper](https://arxiv.org/abs/1705.07204)] 
* **PGD** Towards Deep Learning Models Resistant to Adversarial Attacks 
* **taxonomy of adversaries against DNN classifers?** : The Limitations of Deep Learning in Adversarial Settings [ [paper](https://arxiv.org/abs/1511.07528) ]
* Adversarial Patch **NIPS 2017** [ [paper](https://arxiv.org/abs/1712.09665) ]
* **Deepfool** Deepfool: a simple and accurate method tofool deep neural networks
* **Defence** Mitigating adversarial effects through randomization **defend by randomly padding/resizing/perturbing (denoising)**


# Adversarial Machine Learning Paper

Papers about **[Adversarial Machine Learning](https://en.wikipedia.org/wiki/Adversarial_machine_learning)**.

( **Not** to be confused with Generative adversarial network, GAN )

## The FIRST Paper

In this paper, the author first noticed the existence of *adversarial examples* in image classification application.

* Intriguing properities of neural networkds,2013 , [ [paper](https://arxiv.org/abs/1312.6199) ] 

## Introduction Papers

* Adversarial Machine Learning, 2011,  [ [paper](https://people.eecs.berkeley.edu/~tygar/papers/SML2/Adversarial_AISEC.pdf) ]
* Adversarial examples in the physical world 
* Exploring the space of adversarial images
* Analysis of classifiers’ robustness to adversarial perturbations
* Adversarial Examples Are Not Easily Detected: Bypassing Ten Detection Methods, Nicholas Carlini & David Wagner, [ [code](https://github.com/abhibhav14/adversarial-attacks-papernotes/blob/master/notes/carlini-wagner-bypass.md) ], [[paper](https://arxiv.org/abs/1705.07263)]


## Attacks to Image Classification

In this category, the author usually luanch an attack to an image classifier model, trained using CNN or other machine learning algorithms. A typical way to attack is to add some kind of small **noise** directly to the image (or matrix) and feed it into the target classifier, then get a different (false) classification result.


* **FGSM** : Explaining and Harnessing Adversarial Examples
* **RAND + FGSM** : Practical Black-Box Attacks against Machine Learning
* **CW-Attack** : Towards Evaluating the Robustness of Neural Networks, Nicholas Carlini & David Wagner, [  [paper](https://arxiv.org/abs/1608.04644) ]
* **Traffic Light** : Fooling Vision and Language Models Despite Localization and Attention Mechanism
* Practical Black-Box Attacks against Machine Learning
* **Hack ICLR 2018** : Obfuscated Gradients Give a False Sense of Security : Circumventing Defenses to Adversarial Examples
* Deep neural networks are easily fooled: High confidence predictions for unrecognizable images


###  Attacks to Face Recognition

In this category ...

* Accessorize to a Crime:Real and Stealthy Attacks on State-of-the-Art Face Recognition
* Invisible Mask: Practical Attacks on Face Recognition with Infrared


## Attacks to Malware Detection

* Evading Classifiers by Morphing in the Dark, **black-box attack**
* Adversarial examples for malware detection


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



## Survey

* Adversarial Examples: Attacks and Defenses for Deep Learning, 2018, [ [paper](https://arxiv.org/abs/1712.07107)  ]
* Towards the Science of Security and Privacy in Machine Learning, by McDaniel, Patrick, 



## Stealing Machine Learning Models

* Cracking Classifiers for Evasion: A Case Study on the Google’s Phishing Pages Filter
* Stealing Machine Learning Models via Prediction APIs, **USENIX 2016**




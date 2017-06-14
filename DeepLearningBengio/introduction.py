"""
    Deep Learning (Ian Goodfellow Yoshua Bengrio)
    Chapter 1: Introduction
    Section 1

    Allowing computers to learn from experience and understand
    the world in terms of a heirarchy of concepts, with each concept defined
    in terms of its relation to simpler concepts.

    Avoiding the need for human operators to formally specify all of the
    knowledge that the computer needs.

    The hierarchy of concepts allows the computer to learn complicated concepts
    by building them out of simpler ones.

    If we were to draw a graph illustrating all of these simple tasked layers,
    the graph would be extremely deep. Thus, we call this process
    'Deep Learning'.

    Much of human knowledge is intuitive and is extremely subjective, therefore
    hard for a machine to articulate.

    Hard coding an AI brings many challenges and therefore it is known that AI's
    need to acquire their own knowledge by getting patterns from raw data.

    Logistic Regression: Can recommend ceserean delivery
        * The AI does not examine the patient directly
        * The doctor tells the AI several pieces of useful information
        * Such as:
            - Presence or absence of uterine scar
        * Each piece of information included in the representation of the patient
            is known as a 'Feature'.
        * Logistic Regression learns how each of these features of the patient
            correlates with various outcomes.
        * However, it cannot influence the way that the features are defined
            in any way.
        * If the algorithm was given an MRI scan rather than a report from the
            docter, it would not be able to make any useful predictions.

    Naive Bayes: Seperates legitimate e-mail from spam e-mail.

    Performance of simple machine learning algorithms depends heavily on the
    representation of the data they are given.

    * The choice of Data Representation has a huge effect on the performance
        of machine learning algorithms.

    Many artificial intelligence tasks can be solved by designing the right set
        of features to extract for that task, then providing these features
        to a simple machine learning algorithm.

    Representation Learning: Using Machine Learning to discover not only the
        mapping from representation to output but also the representation
        itself.
            * Learned representations often result in much better performance
                than can be obtained with hand-designed representations.
            * They also allow AI systems to rapidly adapt to new tasks, with
                minimal human intervention.

    Autoencoder: The quintessential example of a representation learning
        algorithm.
        * Combination of an 'encoder' function that converts the input data
            into a different representation, and a 'decoder' function that
            converts the new representation back into the original format.
        * Autoencoders are trained to preserve as much information as possible
            when an input is run through the encoder and then the decoder,
            but are also trained to make the new representation have various
            nice properties.
        * Different kinds of autoencoders aim to achieve different kinds of
            properties.

    When designing features or algorithms for learning features, our goal is
        usually to separate the 'factors of variation' that explain the
        observed data.
        * Factors are simply separate sources of influence.
        * Factors are usually not combined by multiplication
        * Factors are often not quantities that are directly observed.
        Instead:
            - They may exist either as unobserved objects or unobserved
                forces in the physical world that affect observable quantities.
            - They may also exist as constructs of the human mind that provide
                useful simplifying explanations or inferred causes of the
                observed data.

    Types of 'Factors of Variability':
        * When analyzing a speech recording, the factors of variation include
            the speaker's age, their sex, their accent and the words that they
            are speaking.
        * When analyzing an image of a car, the factors of variation include
            the position of the car, its color, and the angle and brightness
            of the sun.

    Deep Learning solves this central problem in representation learning by
        introducing representations that are expressed in terms of other,
        simpler representations.
        * It allows computers to build complex concepts out of smaller and
            simpler concepts.

    Feedforward Deep Network or Multilayer Perceptron(MLP):
        * an MLP is just a mathematical function mapping some set of input
            values to output values.
        * The function is formed by composing many simpler functions.

    The idea of learning the right representation for the data provides on
        perspective on deep learning.
        * Another perspective on deep learning is that depth allows the
            computer to learn a multi-step computer program.
            - Each layer of the representation can be thought of as the state
                of the computer's memory after executing another set of
                instructions in parallel.
            - Networks with greater depth can execute more instructions in
                sequence.
            - Sequential instructions offer great power because later
                instructions can refer back to the results of earlier
                instructions.

    There are two main ways of measuring depth in a model:
        1.) Based on the number of sequential instructions that must be
            executed to evaluate the architecture.
            * The length of the longest path through a flow chart that
                describes how to compute each of the model's outputs given
                its inputs.
        2.) Regards the depth of a model as being not the depth of the
            computational graph but the depth of the graph describing how
            concepts are related to each other.
            * The depth of the flowchart of the computations needed to compute
                the representation of each concept may be much deeper than
                the graph of the concepts themselves.
"""

"""
    1.2.1 The Many Names and Changing Fortunes fo Neural Networks

    Waves of Deep Learning:
        - Cybernetics:   1940s - 1960s
        - Connectionism: 1080s - 1990s
        - Deep Learning: 2006  - Present

    The neural perspective on deep learning is motivated by two main ideas:
        - The brain provides proof by example that intelligent is to reverse
            engineer the computational principles behind the brain and duplicate
            its functionality.
        - It would be deeply interesting to understand the brain and the
            principles that underlie human intelligence, so machine
            learning models that shed light on these basic scientific questions
            are useful apart from their ability to solve engineering
            applications.

    Deep Learning goes beyond the neuroscientific perspective on the current
        breed of machine learning models.
        * Appeals to a more general principle of learning 'Multiple Levels of
            Composition'. Which can be applied in machine learning framework
            that are not necessarily neurally inspired.

    Cybernetics:
        * Development of theories of biological learning and implementations of
            the first models such as the perceptron allowing the training
            of a single neuron.

    Connectionism:
        * Back-propogation to train a neural network with one or two hidden
            layers.

    Deep Learning:
        * Current and third wave

    Cybernetics Explained:
        1.) Simple linear models motivated from a neuroscientific perspective.
        2.) These models were designed to take a set of 'n' input values
            'x1,...,xn'
        3.) Using these inputs, associate them with an output y.
        4.) These models would learn a set of weights 'w1,...,wn'
        5.) Compute their output f(x,w) = x1w1 + ... + xnwn

    Adaptive Linear Element(ADALINE):
        Predicts value of y from f(x)

    Stochastic Gradient Descent:
        - The Training algorithm used to adapt the weights of the ADALINE
        - Slightly modified versions of the stochastic gradient descent algorithm
            remain the dominant training algorithms for deep learning
            models today.

    Linear Models have many limitations:
        - The cannot learn the XOR function.
            * f([0,1],w) = 1
            * f([1,0],w) = 1
            * f([1,1],w) = 0
            * f([0,0],w) = 0

    Rectified Linear Unit: Neural Networks today are based on a model neuron

    Connectionism:
        * Distributed Representation - Idea that each input to a system should
            be represented by many features, and each feature should be involved
            in the representation of many possible inputs.
        * Successful use of Back Propagation -
"""

"""
    1.2.2 Increasing Dataset Sizes
"""

"""
    1.2.3 Increasing Model Sizes
"""

"""
    1.2.3 Increasing Accuracy, Complexity and Real-World Impact
    Convolutional Network for Image Processing

    LSTM sequence model:
        used to model relationships between 'sequences' and other 'sequences'
        rather than just fixed inputs.

    Increasing complexity has been pushed to its logical conclusion with the
        introduction of 'Neural Turing Machines' that learn to read from memory
        cells and write arbitrary content to memory cells.
        * These neural networks can learn simple programs from examples
            of desired behavior.
            Example: They can learn to sort lists given examples of sorted
            and non-sorted lists.

    Domain of Reinforcement Learning:
        * An autonomous agent must learn to perform a task by trial and error
            without any guidance from the human operator.
            (AlphaGo)
        * Also improved the performance of reinforcement learning for robotics.

    Libraries Supporting AI Research:
        * Theano
        * PyLearn2
        * Torch
        * DistBelief
        * Caffe
        * MXNet
        * TensorFlow

    Deep Learning and contributions to other sciences:
        * Convolutional Networks for object recognition provide a model of
            visual processing that neuroscientists can study.
        * Massive amounts of data for making useful predictions in other Types
            of fields.
        * Has been successfully used to predict how molecules will interact
            in order to help pharmaceutical companies design new drugs to
            search for subatomic particles and to automatically parse
            microscope images used to construct 3-D map of the human brain.

"""

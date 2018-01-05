# CNTK 2.2
# Esta NN usa uma camada oculta com dois nós
# trainData_cntk.txt - 120 itens sendo 40 de cada uma das 3 classes
# testData_cntk.txt - 30 itens sendo 10 de cada uma das 3 classes
import numpy as np
import cntk as C
from cntk import Trainer  # to train the NN
from cntk.learners import sgd, learning_rate_schedule, UnitType
from cntk.ops import *  # input_variable() def
from cntk.logging import ProgressPrinter
from cntk.initializer import glorot_uniform
from cntk.layers import default_options, Dense
from cntk.io import CTFDeserializer, MinibatchSource, StreamDef, StreamDefs, INFINITELY_REPEAT

# Função para a exibição de uma matriz e double
def my_print(arr, dec):
    fmt = "%." + str(dec) + "f"  # like %.4f
    for i in range(0, len(arr)):
        print(fmt % arr[i] + '  ', end='')
    print("\n")


def create_reader(path, is_training, input_dim, output_dim):
    return MinibatchSource(CTFDeserializer(path, StreamDefs(
        features=StreamDef(field='attribs', shape=input_dim, is_sparse=False),
        labels=StreamDef(field='species', shape=output_dim, is_sparse=False)
    )), randomize=is_training,
        max_sweeps=INFINITELY_REPEAT if is_training else 1)

# Salva os valores dos pesos
def save_weights(fn, ihWeights, hBiases,
                 hoWeights, oBiases):
    f = open(fn, 'w')
    for vals in ihWeights:
        for v in vals:
            f.write("%s\n" % v)
    for v in hBiases:
        f.write("%s\n" % v)
    for vals in hoWeights:
        for v in vals:
            f.write("%s\n" % v)
    for v in oBiases:
        f.write("%s\n" % v)
    f.close()


def do_demo():
    # create NN, train, test, predict
    input_dim = 4
    hidden_dim = 2
    output_dim = 3

    train_file = "trainData_cntk.txt"
    test_file = "testData_cntk.txt"

    input_Var = C.ops.input(input_dim, np.float32)
    label_Var = C.ops.input(output_dim, np.float32)

    print("Creating a 4-2-3 tanh softmax NN for Iris data ")
    with default_options(init=glorot_uniform()):
        hLayer = C.layers.Dense(hidden_dim, activation=C.ops.tanh, name='hidLayer')(input_Var)
        oLayer = Dense(output_dim, activation=C.ops.softmax, name='outLayer')(hLayer)
    nnet = oLayer

    print("Creating a cross entropy mini-batch Trainer \n")
    ce = C.cross_entropy_with_softmax(nnet, label_Var)
    pe = C.classification_error(nnet, label_Var)

    fixed_lr = 0.05
    lr_per_batch = learning_rate_schedule(fixed_lr, UnitType.minibatch)
    learner = C.sgd(nnet.parameters, lr_per_batch)
    trainer = C.Trainer(nnet, (ce, pe), [learner])

    max_iter = 5000  # Máximo de iterações para o treino
    batch_size = 5   # Define o tamanho para o mini-batch
    progress_freq = 1000  # Exibe o erro a cada n mini-batches

    reader_train = create_reader(train_file, True, input_dim, output_dim)
    my_input_map = {
        input_Var: reader_train.streams.features,
        label_Var: reader_train.streams.labels
    }
    pp = ProgressPrinter(progress_freq)

    print("Starting training \n")
    for i in range(0, max_iter):
        currBatch = reader_train.next_minibatch(batch_size, input_map=my_input_map)
        trainer.train_minibatch(currBatch)
        pp.update_with_trainer(trainer)
    print("\nTraining complete")

    # ----------------------------------

    print("\nEvaluating test data \n")
    reader_test = create_reader(test_file, False, input_dim, output_dim)
    numTestItems = 30
    allTest = reader_test.next_minibatch(numTestItems, input_map=my_input_map)
    test_error = trainer.test_minibatch(allTest)
    print("Classification error on the 30 test items = %f" % test_error)

    # ----------------------------------

    # Faz a predição para uma flor desconhecida
    unknown = np.array([[6.9, 3.1, 4.6, 1.3]], dtype=np.float32)
    print("\nPrevisão  de espécies de Íris para as características de entrada:")
    my_print(unknown[0], 1)  # 1 decimal

    predicted = nnet.eval({input_Var: unknown})
    print("Prediction is: ")
    my_print(predicted[0], 3)  # 3 decimais

    # ---------------------------------

    print("\nTrained model input-to-hidden weights:\n")
    print(hLayer.hidLayer.W.value)
    print("\nTrained model hidden node biases:\n")
    print(hLayer.hidLayer.b.value)

    print("\nTrained model hidden-to-output weights:\n")
    print(oLayer.outLayer.W.value)
    print("\nTrained model output node biases:\n")
    print(oLayer.outLayer.b.value)

    save_weights("weights.txt", hLayer.hidLayer.W.value,
                 hLayer.hidLayer.b.value, oLayer.outLayer.W.value,
                 oLayer.outLayer.b.value)

    return 0  # success


def main():
    cntk = C.__version__
    print("\nDemo Iris Classifications (CNTK " + cntk + ")\n")
    np.random.seed(0)
    do_demo()  # all the work is done in do_demo()

if __name__ == "__main__":
    main()

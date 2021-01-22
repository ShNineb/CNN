# IMPORT
import matplotlib.pyplot as plt
import pandas as pd

"""
# Classe permettant de génerer 4 graphiques de suivit de métriques durant l'entrainement d'un modèle
# Train accuracy, Train loss, Validation accuracy, Validation loss
"""

# def diplayBin():
#     fig, ax = plt.subplots(1, 3, sharey=True, figsize=(16,5))
    
#     for i, (fn, label, c) in enumerate(zip(log_csvs, labels, colors)):
#         csv_path = os.path.join('..', 'C:/Nineb/M2-TAL/CNN/S2_reconnaissanceVoix/Audio-Classification-master/logs', fn)#logs
#         print(csv_path)
#         print(fn)
#         print(c)
#         df = pd.read_csv(csv_path)
#         ax[i].set_title(label, size=16)
#         ax[i].plot(df.accuracy, color=c, label='train')
#         ax[i].plot(df.val_accuracy, ls='--', color=c, label='test')
#         ax[i].legend(loc='upper left')
#         ax[i].tick_params(axis='both', which='major', labelsize=12)
#         ax[i].set_ylim([0,1.0])
    
#     fig.text(0.5, 0.02, 'Epochs', ha='center', size=14)
#     fig.text(0.08, 0.5, 'Accuracy', va='center', rotation='vertical', size=14)
#     plt.show()
    
    

def displayGraph(pathLog,pathSaveGraph):
    """
    # Fonction permettant de creer nos graph de suivi de metriques
    :param pathLog: chemin du CSV contenant nos metrics
    :param pathSaveGraph: chemin de destination pour sauvegarder nos 4 graphiques en jpg
    """

   #data = pd.read_csv("C:/Nineb/M2-TAL/CNN/S2_reconnaissanceVoix/Image-classification-master/audio_classifier/logs/log_moModel.csv")
    data = pd.read_csv(pathLog)
    # split into input (X) and output (Y) variables
    plot(data['epoch'], data['acc'], data['val_acc'], 'TRAIN_VAL_Accuracy', 'Epoch', 'Accuracy', 'upper left',pathSaveGraph)
    plot(data['epoch'], data['loss'], data['val_loss'], 'TRAIN_VAL_Loss', 'Epoch', 'Loss', 'upper left',pathSaveGraph)


def plot(X, Y, Y2, title, xLabel, yLabel, legendLoc, pathSaveGraph):
    """
    # Fonction d'affichage de graph
    :param X: correspond au nombre d'époch
    :param Y: correspond a la courbe accuracy
    :param Y2: correspond a la courbe loss
    :param title: titre du graphique
    :param xLabel: label des abcisses
    :param yLabel: label des ordonnees
    :param legendLoc: legende
    :param pathSaveGraph: chemin de sauvegarde pour les graphiques
    """

   #On trace nos differentes courbes
    plt.plot(Y)
    plt.plot(Y2)
   #titre du graph, legende...
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend(['train', 'val'], loc=legendLoc)
   #Pour avoir un courbe propre qui demarre à 0
    plt.xlim(xmin=0.0, xmax=max(X))
    plt.savefig(pathSaveGraph +'\\' + title)
    plt.figure()
    #plt.show()


def main():
    """
    # Fonction main
    """

    #Definition des chemins d'acces a notre fichier log
    pathLogs = '.\\logs\\log_moModel.csv'
    pathSaveGraph = '.\\graph'
    displayGraph(pathLogs,pathSaveGraph)


if __name__ == "__main__":
    """
    # MAIN
    """
    main()
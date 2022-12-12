def evaluate():
  plt.plot(hist.history["loss"])
  plt.plot(hist.history["val_loss"])
  model.load_weights("transfer_learning.h5")
  print(classification_report(y_val, 
                            np.argmax(model.predict(X_val_p,
                                                       batch_size=32),
                                      axis=1)))
  plt.figure(figsize=(10,5))
  plt.subplot(121)
  plt.plot(hist.history["loss"], "r", label="transfer learning - entrenamiento")
  plt.plot(hist.history["val_loss"], "r--", label="transfer learning - validación")
  plt.xlabel("Épocas")
  plt.title("Pérdida")
  plt.legend()
  plt.subplot(122)
  plt.plot(hist.history["accuracy"], "r", label="transfer learning - entrenamiento")
  plt.plot(hist.history["val_accuracy"], "r--", label="transfer learning - validación")
  plt.xlabel("Épocas")
  plt.title("Accuracy")
  plt.legend()
  
evaluate()
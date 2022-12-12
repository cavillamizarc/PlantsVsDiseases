! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json

#Download Plant desease dataset
! kaggle datasets download -d vipoooool/new-plant-diseases-dataset
! unzip -qq new-plant-diseases-dataset.zip -d ./greeneye/database/DB
! rm new-plant-diseases-dataset.zip
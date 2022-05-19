import pandas as pd 
import os 
from tqdm import tqdm
from sklearn.model_selection import train_test_split


def split_img_label(data_train,data_test,folder_train,folder_test):
    
    if not os.path.exists(folder_train):
        os.mkdir(folder_train)
    if not os.path.exists(folder_test):
        os.mkdir(folder_test)
    
    
    train_ind=list(data_train.index)
    test_ind=list(data_test.index)
    
    
    # Train folder
    for i in tqdm(range(len(train_ind))):
        
        # os.system('cp '+data_train[train_ind[i]]+' ./'+ folder_train + '/'  +data_train[train_ind[i]].split('/')[2])
        os.system('mv '+data_train[train_ind[i]].split('.jpg')[0]+'.txt'+'  ./'+ folder_train + '/'  +data_train[train_ind[i]].split('/')[-1].split('.jpg')[0]+'.txt')
        os.system('mv '+data_train[train_ind[i]]+'  ./'+ folder_train + '/'  +data_train[train_ind[i]].split('/')[-1])
    
    # Test folder
    for j in tqdm(range(len(test_ind))):
        print(data_test[test_ind[j]])
        print(data_test[test_ind[j]].split('.jpg')[0])
        print(data_test[test_ind[j]].split('/')[-1])
        
        # os.system('cp '+data_test[test_ind[j]]+' ./'+ folder_test + '/'  +data_test[test_ind[j]].split('/')[2])
        os.system('mv '+data_test[test_ind[j]].split('.jpg')[0]+'.txt'+'  ./'+ folder_test + '/'  +data_test[test_ind[j]].split('/')[-1].split('.jpg')[0]+'.txt')
        os.system('mv '+data_test[test_ind[j]] + '  ./'+ folder_test + '/'  +data_test[test_ind[j]].split('/')[-1])



dirs = ["16_10_21_center_400imgs"]

for d in dirs:
    data_path = '../arama_dataset/%s/' % d
    train_path = '../arama_dataset/%s/train' %d
    val_path = '../arama_dataset/%s/val' %d

    print(data_path)

    list_img=[img for img in os.listdir(data_path) if img.endswith('.jpg')==True]
    list_txt=[img for img in os.listdir(data_path) if img.endswith('.txt')==True]


    path_img=[]

    for i in range (len(list_img)):
        path_img.append(data_path+list_img[i])
        
    df=pd.DataFrame(path_img)

    print(df)

    # split 
    data_train, data_test, labels_train, labels_test = train_test_split(df[0], df.index, test_size=0.10, random_state=42)

    # Function split 
    split_img_label(data_train, data_test, train_path, val_path)

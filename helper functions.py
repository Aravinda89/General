# Binary labels

# Show batch of images using dataframe
def show_batch(df, source_dir, show_labels=False):
    df = shuffle(df)
    df.reset_index(drop=True, inplace=True)
    plt.figure(figsize=(12, 12))
    for n in range(9):
        ax = plt.subplot(3, 3, n+1)
        filename = df.iloc[n, 0]
        img = load_img(source_dir+ filename, target_size=(224, 224))
        if show_labels:
            labels = list(df.iloc[n,:][df.iloc[n,:]==1].to_dict().keys())
        plt.imshow(img)
        plt.xlabel(labels)
        plt.axis('on')

# Value counts
def value_count(df):

    index=[]
    counts=[]
    for i in list(df.columns[1:]):
        index.append(i)
        counts.append(df[i].value_counts().to_dict())
    index_re = [i for i in index]

    #key_map = dict(zip(index, index_re))
    #df = pd.DataFrame(counts, index=index_re)
    df = pd.DataFrame(counts)
    original_df = df.copy()
    original_df['Disease_Type']=index
    original_df = original_df.rename(columns={0:"Negative", 1:"Positive"})
    original_df = original_df.sort_values(by=['Positive'], ascending=False)
    original_df = original_df[['Disease_Type','Negative', 'Positive']]
    
    df = df.rename(columns={0:"Negative",1:"Positive"})
    df = df.sort_values(by=['Positive'],ascending=False)

    ax = df.plot.bar(rot=0,title ="Positive/Negative Count",figsize=(20,11),legend=True, fontsize=12)
    ax.set_yticks([i for i in range(0,df['Negative'].max()+1000,1000)])
    ax.set_yticklabels([i for i in range(0,df['Negative'].max()+1000,1000)], fontsize=8)
    ax.set_xlabel("Disease_Type",fontsize=14)
    ax.set_ylabel("Count",fontsize=14)
    ax.grid(True,linestyle='--',color='0.75')
    
    return original_df


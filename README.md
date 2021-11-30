# DVC Sample Project
Simple project to explore the capabilities of [DVC](https://dvc.org/).

Dataset is from the [latest (Nov 2021) Kaggle Tabular Competition](https://www.kaggle.com/c/tabular-playground-series-nov-2021)

Code and (meta)data tracking is done by GitHub. DVC works under the hood to store different versions of the data in the cloud, Amazon S3 in this case. 

## Reproducibility

To showcase how easy to reproduce work done using DVC in order to run everything from scratch you just have to run:

```
dvc repro
```

To run hyperparameter tuning you just have to modify any parameter in the `params.yaml` file and then run:

```
dvc repro
dvc metrics show
```

DVC automatically knows what steps to cache or execute in order to run only the necessary steps.

To visualize the pipeline DAG run:

```
dvc dag
```

You will see something like this:

```
    +--------------------+ 
    | data/train.csv.dvc | 
    +--------------------+ 
              *            
              *            
              *            
        +------------+     
        | data_split |     
        +------------+     
              *            
              *            
              *            
        +-----------+      
        | normalize |      
        +-----------+      
         **        **      
       **            *     
      *               **   
+-------+               *  
| train |             **   
+-------+            *     
         **        **      
           **    **        
             *  *          
        +----------+       
        | evaluate |       
        +----------+       
```

## Extending functionality

### Add data

To add source datasets:

```
dvc add file.csv
```

The rest of the intermediate files are added automatically by DVC when you define them as outputs in `dvc.yaml`.

### Add steps to the pipeline

All the steps in the pipeline, their inputs and outputs must be defined in `dvc.yaml`.
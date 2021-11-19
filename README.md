# swedenweather
This is the task to load the weather(Pressure and Temperature) data into two different big query tables using python, Apache beam and Dataflow
![image](https://user-images.githubusercontent.com/30459052/142369621-7fdf5f90-d2e7-4d70-9413-8e2f50bd8ef7.png)


**Note: Make sure BQ Dataset & Regional Cloud Bucket are in the SAME region.**

**Loading Air Pressure data:**


**Note:** I’ll create three different tables in big query as I can see three different schemas (1756, 1859 and General Schema)

1. Create an empty table us-central1 dataset in BigQuery with this schema using.
    
    **a. # Schema_1756**  
    bq mk YOUR_DATASET_NAME.air_batch_processing_1756 year:STRING,month:STRING,day:STRING, pressure_morning:STRING,barometer_temperature_observations_1:STRING, pressure_noon:STRING,barometer_temperature_observations_2:STRING,pressure_evening:STRING,barometer_temperature_observations_3:STRING
    
    **b. # Schema_1859**
    bq mk YOUR_DATASET_NAME.air_batch_processing_1859 year:STRING,month:STRING,day:STRING,pressure_morning:STRING,thermometer_observations_1:STRING, air_pressure_reduced_to_0_degC_1:STRING,pressure_noon:STRING,thermometer_observations_2:STRING,air_pressure_reduced_to_0_degC_2:STRING,pressure_evening:STRING, thermometer_observations_3:STRING,air_pressure_reduced_to_0_degC_3:STRING
    
    **c. #Schema_General**
    bq mk air_pressure_observation.air_pressure_general_schema year:STRING,month:STRING,day:STRING,pressure_morning:STRING,pressure_noon:STRING,pressure_evening:STRING

2. Create a Regional Bucket named air-pressure-templates in us-central1 region.

3. Upload dataflow.zip to cloud shell and unzip it using unzip dataflow.zip,

4. Change directory to dataflow.

5. Copy Metadata file named SKU_Data_air_pressure_general_metadata to gs://air-pressure- templates/templates/ 

6. Run pip3 install -r requirements.txt –user.

7. Obtains user access credentials & authenticate using gcloud auth application-default login.

8. Run the below command to create a Dataflow template.


      **a. # Schema_1756**
      python3 load-to-bq-pressure-1756.py --runner DataFlowRunner --project $DEVSHELL-PROJECT-ID --temp_location gs://air-pressure-templates/temp --staging_location gs://air-pressure -templates/staging --region us-central1 --template_location gs://air-pressure-templates/templates/SKU_Data_air_pressure_general  --experiment=use_beam_bq_sink

      **b. # Schema_1859**
      python3 load-to-bq-pressure-1859.py --runner DataFlowRunner --project $DEVSHELL-PROJECT-ID --temp_location gs://air-pressure-templates/temp --staging_location gs://air-pressure -templates/staging --region us-central1 --template_location gs://air-pressure-templates/templates/SKU_Data_air_pressure_general  --experiment=use_beam_bq_sink

      **c. #Schema_General**
      python3 load-to-bq-pressure-general.py --runner DataFlowRunner --project $DEVSHELL-PROJECT-ID --temp_location gs://air-pressure-templates/temp --staging_location gs://air-pressure -templates/staging --region us-central1 --template_location gs://air-pressure-templates/templates/SKU_Data_air_pressure_general  --experiment=use_beam_bq_sink

**Loading Temperature data:**

**Note: I’ll create three different tables in big query as I can see three different schemas (1756, 1859 and General Schema)**

1. Create an empty table us-central1 dataset in BigQuery with this schema using.
    **a. # temp_Schema_1756  **
        
        bq mk YOUR_DATASET_NAME.temp_batch_processing_1756 year:STRING, month:STRING, day:STRING, pressure_morning:STRING, pressure_noon:STRING, pressure_evening:STRING 
    
    **b. # temp_Schema_1859**
    
        **bq mk YOUR_DATASET_NAME.temp_batch_processing_1859 year:STRING,month:STRING, day:STRING, pressure_morning:STRING, pressure_noon:STRING, pressure_evening:STRING, tmin_3:STRING, tmax:STRING**
    
    **c. #temp_Schema_General**
    
    bq mk air_pressure_observation.air_pressure_general_schema year:STRING,month:STRING,day:STRING,pressure_morning:STRING,pressure_noon:STRING,pressure_evening:STRING,tmin_3:STRING,tmax:STRING,estimatedDiurnalMean:STRING

2. Create a Regional Bucket named temp-pressure-templates in us-central1 region.

3. Upload dataflow.zip to cloud shell and unzip it using unzip dataflow.zip,

4. Change directory to dataflow.

5. Copy Metadata file named SKU_Data_temp_pressure_general_metadata to gs://temp-pressure- templates/templates/ 

6. Run pip3 install -r requirements.txt –user.

7. Obtains user access credentials & authenticate using gcloud auth application-default login.

8. Run the below command to create a Dataflow template.

**a. # temp_Schema_1756**
    
    python3 load-to-bq-temp-1756.py --runner DataFlowRunner --project $DEVSHELL-PROJECT-ID --temp_location gs://temp-pressure-templates/temp --staging_location gs://temp-pressure -templates/staging --region us-central1 --template_location gs://temp-pressure-templates/templates/SKU_Data_temp_pressure_general  --experiment=use_beam_bq_sink
    
**b. # temp_Schema_1859**

python3 load-to-bq-temp-1859.py --runner DataFlowRunner --project $DEVSHELL-PROJECT-ID --temp_location gs://temp-pressure-templates/temp --staging_location gs://temp-pressure -templates/staging --region us-central1 --template_location gs://temp-pressure-templates/templates/SKU_Data_temp_pressure_general  --experiment=use_beam_bq_sink

**c. # temp_Schema_General**

python3 load-to-bq-temp-general.py --runner DataFlowRunner --project $DEVSHELL-PROJECT-ID --temp_location gs://air-pressure-templates/temp --staging_location gs://temp-pressure -templates/staging --region us-central1 --template_location gs://temp-pressure-templates/templates/SKU_Data_temp_pressure_general  --experiment=use_beam_bq_sink


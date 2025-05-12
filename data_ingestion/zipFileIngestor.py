from data_ingestion.data_ingestor import DataIngestor
import pandas as pd
import os
import zipfile

#Concrete class for ZIP Ingestion
class ZipFileIngestor(DataIngestor):
    
    def ingest(self,file_path:str)->pd.DataFrame:
        """
        Extract a .zip file and returns the content as a pandas dataframe. 
        """
        
        #Ensure the file is a .zp file
        if not file_path.endswith(".zip"):
            raise ValueError("The provided file is not a .zip file")
        
        #Extract the zip file
        with zipfile.ZipFile(file_path,'r') as zip_ref:
            zip_ref.extractall("extracted_data")
            
        #Find the extarcted CSV File(assuming there is 1 CSV file inside the zip)
        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]
        
        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV File found in the zip")
        
        if len(csv_files) > 1:
            raise ValueError("Multple CSV files found. Please upload zip with 1 csv")
        
        #Read the CSV into DataFrame
        csv_file_path = os.path.join("extracted_data",csv_files[0])
        df = pd.read_csv(csv_file_path)
        
        #return the dataFame
        return df
        
        
    
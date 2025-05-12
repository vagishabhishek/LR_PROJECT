import pandas as pd
from data_ingestion.data_ingestor import DataIngestor

#Concrete class for CSV File Ingestion
class CsvFileIngestor(DataIngestor):
    
    def ingest(self,file_path:str)->pd.DataFrame:
        """
        Read a csv file nd return a dataFrame
        """
        
        #Check if file type is .csv 
        if not file_path.endswith(".csv"):
            raise ValueError("Not a CSV file. Upload a csv file")
        
        #read the csv file
        df = pd.read_csv(file_path)
        
        #return the dataframe
        return df
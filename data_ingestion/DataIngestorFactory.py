from data_ingestion.csvFileIngestor import CsvFileIngestor
from data_ingestion.zipFileIngestor import ZipFileIngestor
from data_ingestion.data_ingestor import DataIngestor
import os

#Data Ingestion Factory
class DataIngestorfactory:
    
    @staticmethod
    def get_file_extension(file_path:str)->str:
        """
        returns file extension of file being uploaded for ingestion
        """
        
        #check if its a valid path
        if not os.path.isfile(file_path):
            raise ValueError("No such File found")
        
        else:
            #return file extension
            return file_path.split(".")[-1]
        
    @staticmethod
    def get_ingestor(file_path:str)-> DataIngestor:
        """
        Returns data ingestor according to the file path being provided
        """
        file_extension = DataIngestorfactory.get_file_extension(file_path)
        
        if file_extension == "zip":
            return ZipFileIngestor()
        
        if file_extension == "csv":
            return CsvFileIngestor()
        
        else:
            raise Exception("File type is not supported currently") 
        
        
if __name__ == "__main__":
    file_path = r"D:\python_practice\EDA\Churn_Modelling.csv"
    data_ingestor = DataIngestorfactory.get_ingestor(file_path)
    
    df = data_ingestor.ingest(file_path)
    print(df.head())
    
          
        


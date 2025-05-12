from abc import abstractmethod,ABC
import pandas as pd
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path :str) ->pd.DataFrame:
        """
        Abstract method to ingest data from a given file
        """
        pass
    
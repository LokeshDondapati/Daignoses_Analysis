# importing library pandas
import pandas as pd

# dataset url
url = "https://raw.githubusercontent.com/LokeshDondapati/project1/main/HIV_AIDS_Diagnoses_by_Neighborhood__Age_Group__and_Race_Ethnicity.csv"


class Datasummary:
    """
    class to get data from url and to showcase data.

    Parameters:
    - url (str): url of dataset."""

    def __init__(self, url):
        self.url = url

    def readdata(self, url):
        """For loading dataset, datset was uploaded to GitHub and with the gitHub url all  the data is being fetched"""
        data = pd.read_csv(self.url)
        return data

    def second_readdata(self):
        """
        Reads the second dataset from a predefined URL.

        Returns:
        - pd.DataFrame: Second dataset.
        """
        url = "https://raw.githubusercontent.com/LokeshDondapati/HIV-AIDS-Diagnoses-Analysis/main/Datasets/HIV_AIDS_Diagnoses_by_Neighborhood__Sex__and_Race_Ethnicity_20231126.csv"
        data = pd.read_csv(url)
        return data

    def datasummary(self):
        """
        Gives rows/use cases and columns/attributes.

        Parameters:
        -
        Method:
        readdata function called to fetch required data
        Returns:
        dict: number of use cases, attributes and data types.
        """
        # Method that gives data of rows and columns
        data = self.readdata(url)
        # Calculate the number of use cases
        num_use_cases = data.shape[0]

        # Calculate the number of attributes
        num_attributes = data.shape[1]

        # List data types for each attribute
        data_types = data.dtypes

        # Display the results
        print("Use Cases:", num_use_cases)
        print("Attributes:", num_attributes)
        print("Data Types for Attribute:", data_types)
        result = {
            "Use Cases": num_use_cases,
            "Attributes": num_attributes,
            "Data Types for Attribute": data_types,
            "dataframe": data,
        }
        return result

    def second_dataset_summary(self):
        """
        Gives rows/use cases and columns/attributes.

        Parameters:
        -
        Method:
        readdata function called to fetch required data
        Returns:
        dict: number of use cases, attributes and data types.
        """
        # Method that gives data of rows and columns
        data = self.second_readdata()
        # Calculate the number of use cases
        num_use_cases = data.shape[0]

        # Calculate the number of attributes
        num_attributes = data.shape[1]

        # List data types for each attribute
        data_types = data.dtypes

        # Display the results
        print("Use Cases:", num_use_cases)
        print("Attributes:", num_attributes)
        print("Data Types for Attribute:", data_types)
        result = {
            "Use Cases": num_use_cases,
            "Attributes": num_attributes,
            "Data Types for Attribute": data_types,
        }
        return result

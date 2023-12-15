import pandas as pd
import pandas_read_xml as pdx

historicos = []

historicos_path = "" # Set the historicos path to be processed
historicos_root_path = [] # Define each root tag to narrow down what information will be processed

number_of_historicos = 0 # Define the number of historicos that will be read

for i in range(number_of_historicos):
    historicos.append(
        pdx.fully_flatten(
            pdx.read_xml(
                f"{historicos_path}/historico_{i}.xml" 
                # This string points to a historico with the following namming patter 'historico_0.xml'
                , historicos_root_path
            )
        )
    )

historico = pd.concat(historicos, ignore_index=True)
historico.to_csv("historicos.csv")
import json

from azureml.core import Webservice
from azureml.core import Workspace


#def main(service):
def main():
    # Creating input data
    print("Creating input data")
    data = {"data": [[ 1,2,3,4 ], [ 10,9,8,7 ]]}
    input_data = json.dumps(data)



    ws = Workspace("2e5fff2c-fb7d-4c24-965b-5f71a1b89d60", "hlazmlworkspace1-rsg1", "hlazmlworkspace1")
    service = Webservice(ws,"unityhealthmlops-main")

    # Calling webservice
    print("Calling webservice")
    output_data = service.run(input_data)
    predictions = output_data.get("predict")
    assert type(predictions) == list
    print("Input: {}   prediction: {}".format(input_data, predictions))


if __name__ == "__main__":
    main()

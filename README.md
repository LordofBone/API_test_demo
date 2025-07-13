## API test example

### How to run the API tests
To run the API tests, you need to have Python installed along with the required packages. Follow these steps:

1. **Clone the Repository**: If you haven't already, clone the repository to your local machine:
   ```bash
   git clone https://github.com/LordofBone/API_test_demo
   ```
2. **Install Dependencies**: Make sure you have the required packages installed. You can do this by running:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Tests**: Use the following command to run the API tests:
   ```bash
   pytest --html=reports/report.html --self-contained-html
    ```
   
4. **View the Report**: After running the tests, you can view the generated report in `reports/report.html`.

### Acceptance Criteria covered:
* #### Name = "Carbon credits" ✅
   ``` bash
   pytest test_api.py::test_api_response_name
   ```

* #### CanRelist = true ✅
   ``` bash
   pytest test_api.py::test_api_response_can_list
   ```

* #### The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category" ✅
   ``` bash
   pytest ./test_api.py::test_promotions_description
   ```
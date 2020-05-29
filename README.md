# ReportPortal practice
Just a practice of the [ReportPortal.io](https://reportportal.io) tool

## To execute tests
1. Install docker;
2. Start report_portal `start_rp.sh`
3. Open RP `localhost:8080`
4. Go to profile and copy `Access token`
5. Paste token into the `pytest.ini` - `rp_uuid`
6. Run tests `run_tests.sh`
7. Check results in RP UI

### [Video](https://drive.google.com/file/d/1xX_7hwz_cA4EpXnCQNJh1xbTf8yXiR-H/view?usp=sharing)

## Note
I prefer [Allure](http://allure.qatools.ru) report more cause it's faster and easier. RP takes a lot of RAM and hard to setup. Also it's very uncomfortable to use it with python cause there are no docs about it need to develop new bicycles...  
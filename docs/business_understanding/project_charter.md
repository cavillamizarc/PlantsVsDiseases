# Project Charter

## Business background

This project is aimed to improve the crops yield of several plantations arround Bogotá City in Colombia. This will be obtained through the automatic identification od several classic diseases that affect the plants around the city.



////Who is the client, what business domain the client is in.
////* What business problems are we trying to address?

## Scope

The solution delivered to the farmers will require a set of cameras with automatic triggerin each (day/week) (To be defined). The photos taken by this cameras will be feeded into an API that will store them in a data base, analize them, and send an alert to the customer in case a disease is detected

//* What data science solutions are we trying to build?
//* What will we do?
//* How is it going to be consumed by the customer?

## Personnel
	* GreenEyes:
		* Project lead: César Villamizar
		* PM: Johan Gomez
		* Data scientist: Camilo Villalba
		* Account manager: Geraldine Cañas
	* Client:
		* Crops on the outside of Bogota
	
## Metrics

### Baseline
The baseline of this project is defined by the data collected in the Bussiness Understanding phase. (TODO)

### Quantitative Metrics
* Plant disease rate of true possitive detection.
* Average lead time for a desease detection.
* Crop yield over a period with AI assisted supervision Vs Crop yield without suppervision
* Number of plant individuals with advanced disease status undetected
* Rate of disease spreading

### Quanlitative Metrics
* Decrease the ammount of manual supervision required in order to detect on short notice an advanced case of the objective diseases

### Methodology
* Keep a set of different crops, each divided by supervised and unsupervised. The supervised groups will have a set of cameras

## Plan

* Bussines understanding (14/10/2022 - 28/10/2022): The goal of this phase is to collect the requiered information in order to understand the requirements of the customer. Some points of interest are:
  * Most commmon plant diseasses.
  * Most impactfull plant diseasses.

* Data collection

## Architecture
//* Data
//  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)

//* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
//  * all the data,
//  * after some pre-aggregation on-prem,
//  * Sampled data enough for modeling

//* What tools and data storage/analytics resources will be used in the solution e.g.,
//  * ASA for stream aggregation
//  * HDI/Hive/R/Python for feature construction, aggregation and sampling
//  * AzureML for modeling and web service operationalization
//* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
//  * How will the customer use the model results to make decisions
//  * Data movement pipeline in production
//  * Make a 1 slide diagram showing the end to end data flow and decision architecture
//    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication
* Metings are to be held with the client every other monday in order to show advances and raise questions.
* Daily meetings are to be held amongst the development team.

### Key contacts
  * Claudia Bohorquez (local farmer). (+57) 300 1234567
  * Geraldine Cañas (Account manager). (+57) 301 9876543

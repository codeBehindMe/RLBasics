FROM jupyter/datascience-notebook
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt
RUN npm install --save plotlywidget


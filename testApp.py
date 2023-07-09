from models.extractStruct import DatabaseRepresentation
from OpenAiAssistant.QueryGenrator import DBAnalyzer

import sqlite3


def main():

    dbr = DatabaseRepresentation('northwind.db')
    dbr.generate_db_representation()

    DBAnalyzer.AnalyseTables(dbr.db_representation)

    

main()

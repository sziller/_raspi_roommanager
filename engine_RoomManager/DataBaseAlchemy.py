import time
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData, Column, Float, Integer, String, JSON
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker

from cryptography import HashFunctions as HaFu

# from EngineProcesses import (HelperFunctions as HeFu,
#                              HashFunctions as HaFu)

Base = declarative_base()


def createSession(db_path: str, base=Base):
    """=== Function name: createSession ================================================================================
    ============================================================================================== by Sziller ==="""
    engine = create_engine('sqlite:///{}'.format(db_path), echo=False, poolclass=NullPool)
    base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session()





# CLASS definitions ENDED                                                                   -   ENDED   -
# CLASS assignment to tables START                                                          -   START   -
OBJ_KEY = {"measurements": Measurement}
# CLASS assignment to tables ENDED                                                          -   ENDED   -


def ADD_rows_to_table(primary_key: str,
                      data_list: list,
                      db_table: str,
                      session_in: object or None = None):
    """
    @param primary_key: 
    @param data_list: 
    @param db_path: 
    @param db_table: 
    @param style: 
    @param session_in: 
    @return: 
    """
    session = session_in
    added_primary_keys = []
    global OBJ_KEY
    RowObj = OBJ_KEY[db_table]
    for data in data_list:
        # there are cases:
        # - a. when primary key exists before instance being added to DB
        # - b. primary key is generated from other incoming data on instantiation
        if primary_key in data:  # a.: works only if primary key is set and included in row to be created!
            if not session.query(RowObj).filter(getattr(RowObj, primary_key) == data[primary_key]).count():
                newrow = RowObj.construct(d_in=data)
                session.add(newrow)
                added_primary_keys.append(data[primary_key])
        else:
            # this is the general case. <data> doesn't need to include primary key:
            # we check if primary key having been generated on instantiation exists.
            newrow = RowObj.construct(d_in=data)
            if not session.query(RowObj).filter(getattr(RowObj, primary_key) == getattr(newrow, primary_key)).count():
                session.add(newrow)
    session.commit()
    if not session_in:
        session.close()
    return added_primary_keys


def MODIFY_multiple_rows_by_column_to_value(
        filterkey: str,
        filtervalue_list: list,
        target_key: str,
        target_value,
        db_table: str,
        session_in: object or None = None):
    """=== Function name: db_REC_modify_multiple_rows_by_column_to_value ===============================================
    USE THIS IF THE NEW VALUES THE CELLS MUST TAKE ARE IDENTICAL!!!
    This function deals with the USERs DB Table!!!
    @param filterkey: str - name of column, in which filtervalues will be looked for
    @param filtervalue_list: list - list of values of rows to be deleted
    @param target_key: str - name of the column, whose value will be modified
    @param target_value: any data to be put into multiple cell
    @param db_path: str - the actual DataBase name the engine uses. Different for SQLite and PostGreSQL
    @param db_table: str - name of the table you want to write
    @param style: str - to distinguish path handling, enter DB style : PostGreSQL or SQLite
    @param session_in: obj - a precreated session. If used, it will not be closed. If not entered, a new session is
                                                    created, which is closed at the end.
    @return:
    ============================================================================================== by Sziller ==="""
    session = session_in
    global OBJ_KEY
    RowObj = OBJ_KEY[db_table]
    for filtervalue in filtervalue_list:
        session.query(RowObj).filter(getattr(RowObj, filterkey) == filtervalue).update({target_key: target_value})
    session.commit()
    if not session_in:
        session.close()


def MODIFY_multiple_rows_by_column_by_dict(filterkey: str,
                                           mod_dict: dict,
                                           db_table,
                                           session_in: object or None = None):
    """
    
    @param filterkey: 
    @param mod_dict: 
    @param db_path: 
    @param db_table: 
    @param style: 
    @param session_in:
    @return: 
    """

    session = session_in
    global OBJ_KEY
    RowObj = OBJ_KEY[db_table]
    for filtervalue, sub_dict in mod_dict.items():
        session.query(RowObj).filter(getattr(RowObj, filterkey) == filtervalue).update(sub_dict)
    session.commit()
    if not session_in:
        session.close()


def QUERY_entire_table(ordered_by: str,
                       db_table: str,
                       session_in: object or None = None) -> list:
    """=== Function name: QUERY_entire_table =========================================================================
    Function returns an entire DB table, defined by args.
    This function deals with the entered DB Table!!!
    @param ordered_by:
    @param db_path:
    @param db_table:
    @param style:
    @param session_in:
    @return: list of rows in table requested.
    ========================================================================================== by Sziller ==="""
    session = session_in
    global OBJ_KEY
    RowObj = OBJ_KEY[db_table]
    results = session.query(RowObj).order_by(ordered_by).all()
    result_list = [_.return_as_dict() for _ in results]
    session.commit()
    if not session_in:
        session.close()
    return result_list


def QUERY_rows_by_column_filtervalue_list_ordered(filterkey: str,
                                                  filtervalue_list: list,
                                                  ordered_by: str,
                                                  db_table: str,
                                                  session_in: object or None = None) -> list:

    """=== Function name: QUERY_rows_by_column_filtervalue_list_ordered =============================================
    This function deals with the entered DB Table!!!
    @param filterkey:
    @param filtervalue_list:
    @param ordered_by:
    @param db_table:
    @param session_in:
    @return:
    ============================================================================================== by Sziller ==="""
    session = session_in
    global OBJ_KEY
    RowObj = OBJ_KEY[db_table]
    '''
    rec_results = []
    for filtervalue in filtervalue_list:
        rec_subresults = session.query(RowObj).filter(getattr(RowObj, filterkey) == filtervalue).order_by(ordered_by).all()
        rec_results += rec_subresults
        '''
    # rec_results = session.query(RowObj).filter(getattr(RowObj, filterkey) in filtervalue_list).order_by(ordered_by).all()
    # rec_results = session.query(RowObj).filter(RowObj.hash_hxstr.in_(tuple(filtervalue_list)))

    results = session.query(RowObj).filter(getattr(RowObj, filterkey).in_(tuple(filtervalue_list))).order_by(ordered_by)
    result_list = [_.return_as_dict() for _ in results]
    session.commit()
    if not session_in:
        session.close()
    return result_list


if __name__ == "__main__":
    pass

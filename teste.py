from sqlalchemy import create_engine

from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import sessionmaker


class DisciplinaDAO:

    def __init__(self):
        engine = create_engine("mysql+mysqlconnector://root:uniceub@localhost/bd_escola?charset=utf8mb4")

        DB = automap_base()

        DB.prepare(engine, reflect=True)

        self.ta_mat = DB.classes.ta_mat

        self.tb_alu = DB.classes.tb_alu

        self.tb_dis = DB.classes.tb_dis

        session_factory = sessionmaker(bind=engine)

        self.ses = session_factory()

    def create(self, disc):
        self.ses.add(disc)

        self.ses.commit()

    def readAll(self):
        disc = self.ses.query(self.tb_dis).all()

        return disc

    def readById(self, id):
        disc = self.ses.query(self.tb_dis).filter_by(idt_dis=id).first()

        return disc

    def readByName(self, name):
        disc = self.ses.query(self.tb_dis).filter(self.tb_dis.nme_dis.ilike('%' + name + '%')).all()

        return disc

    def update(self):
        self.ses.commit()

    def delete(self, disc):
        self.ses.delete(disc)

        self.ses.commit()

    def __del__(self):
        self.ses.close()


# 2

from dao import dao as disciplinaDAO


def testeInc():
    dao = disciplinaDAO.DisciplinaDAO()

    disc = dao.tb_dis()

    disc.sgl_dis = 'IA'

    disc.nme_dis = 'Inteligencia Artificaial'

    disc.num_ch_dis = 85

    dao.create(disc)


def testeLer():
    dao = disciplinaDAO.DisciplinaDAO()

    for c in dao.readAll():
        print(c.nme_dis)


def testeLerNome():
    dao = disciplinaDAO.DisciplinaDAO()

    for c in dao.readByName('e'):
        print(c.nme_dis)


def testeAlterar():
    dao = disciplinaDAO.DisciplinaDAO()

    disc = dao.readById(4)

    disc.sgl_dis = 'ETC'

    dao.update()


def testeExcluir():
    dao = disciplinaDAO.DisciplinaDAO()

    disc = dao.readById(6)

    dao.delete(disc)

from typing import Optional
import can
import cantools
from can.interfaces import vector
from can import typechecking

MASTER_TO_SLAVE_MSG = "Master_to_slave_standard_msg"

class MasterVectorCAN():
    def __init__(self, channel, dbc_file_path):
        self.channel = channel
        self.dbc_file_path = dbc_file_path
        self.bus = None

        self.db = None
    def open(self):
        """
        Ouvre le bus de communication.
        """
        try:
            self.bus = vector.VectorBus(bitrate=500000, channel=self.channel,app_name="python-can")
            return True
        except Exception as e:
            print(f"Erreur lors de l'ouverture du bus : {e}")
            return False

    def send(self, counter, Command_sg,Num_selector,Table_Selector, extended_id=False):
        """
        Envoie un message sur le bus de communication.

        Args:
            message_id (int): L'identifiant du message CAN.
            data (bytes): Les données à envoyer.
            extended_id (bool, optional): Si True, utilise un identifiant étendu (29 bits). Sinon, utilise un identifiant standard (11 bits). Par défaut, False.

        Returns:
            bool: True si l'envoi a réussi, False sinon.
        """
        try:

            data = {"Counter":counter,"Command_sg":Command_sg,"Num_selector":Num_selector,"Table_Selector":Table_Selector}
            can_msg = self.encode_message(MASTER_TO_SLAVE_MSG,data=data)
            self.bus.send(can_msg)
            return True
        except Exception as e:
            print(f"Erreur lors de l'envoi du message : {e}")
            return False

    def receive(self, timeout=None):
        """
        Reçoit un message depuis le bus de communication.

        Args:
            timeout (float, optional): Temps d'attente maximal en secondes. Si None, la fonction bloque jusqu'à ce qu'un message soit reçu. Par défaut, None.

        Returns:
            can.Message: Le message reçu, ou None en cas d'expiration du timeout.
        """
        try:
            return self.bus.recv(timeout=timeout)
        except Exception as e:
            print(f"Erreur lors de la réception du message : {e}")
            return None

    def load_dbc_file(self):
        """
        Charge la configuration depuis un fichier DBC.

        Returns:
            bool: True si le chargement a réussi, False sinon.
        """
        try:
            self.bus.set_filters([{"dbc": self.dbc_file_path}])
            self.db = cantools.database.load_file(self.dbc_file_path)
            self.master_msg = self.db.get_message_by_name(MASTER_TO_SLAVE_MSG)
            return True
        
        except Exception as e:
            print(f"Erreur lors du chargement du fichier DBC : {e}")
            return False


    def close(self):
        """
        Ferme le bus de communication.
        """
        if self.bus is not None:
            self.bus.shutdown()
            self.bus = None

if __name__ == "__main__":
    channel = 0  # Channel du bus CAN Vector (peut varier selon la configuration matérielle)
    dbc_file_path = "C:\\Users\\MPI4ABT\\Documents\\MATLAB\\Can_db.dbc"
    interface = "vector"
    vector_can = MasterVectorCAN(channel, dbc_file_path)
    print("Instantiated")
    if vector_can.open():
        print("Opened")
        vector_can.load_dbc_file()

        # Exemple d'envoi de données
        message_id = 0x123
        data = b'\x01\x02\x03\x04\x05\x06\x07\x08'
        vector_can.send(counter=b'x01',Command_sg=b'x01',Num_selector=b'0011',Table_Selector=b'x01',extended_id=False)

        # Exemple de réception de données avec un timeout de 1 seconde
        received_message = vector_can.receive(timeout=1)
        if received_message:
            print(f"Message reçu : {received_message}")

        vector_can.close()
import streamlit as st

# Definisi class Node untuk BST
class Node:
    def __init__(self, room_number):
        self.room_number = room_number
        self.left = None
        self.right = None

# Definisi class BST untuk mengelola kamar
class BST:
    def __init__(self):
        self.root = None

    def insert(self, room_number):
        self.root = self._insert_recursive(self.root, room_number)

    def _insert_recursive(self, node, room_number):
        if node is None:
            return Node(room_number)
        if room_number < node.room_number:
            node.left = self._insert_recursive(node.left, room_number)
        else:
            node.right = self._insert_recursive(node.right, room_number)
        return node

    def in_order_traversal(self):
        room_list = []
        self._in_order_traversal_recursive(self.root, room_list)
        return room_list

    def _in_order_traversal_recursive(self, node, room_list):
        if node:
            self._in_order_traversal_recursive(node.left, room_list)
            room_list.append(node.room_number)
            self._in_order_traversal_recursive(node.right, room_list)


# Global variable untuk menyimpan data kamar dan transaksi
bst = BST()
transactions = []


def input_room_data():
    st.header("Input Data Kamar")
    room_number = st.number_input("Nomor Kamar")
    bst.insert(room_number)
    st.success("Data kamar telah ditambahkan.")


def display_room_status():
    st.header("Status Kamar")
    room_list = bst.in_order_traversal()
    st.write("Daftar Kamar:", room_list)


def input_transaction_data():
    st.header("Input Data Transaksi")
    room_number = st.number_input("Nomor Kamar")
    check_in_date = st.date_input("Tanggal Check-in")
    check_out_date = st.date_input("Tanggal Check-out")
    transaction = {
        "room_number": room_number,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date
    }
    transactions.append(transaction)
    st.success("Data transaksi telah ditambahkan.")


def display_transaction_history():
    st.header("Riwayat Transaksi")
    for i, transaction in enumerate(transactions):
        st.write(f"Transaksi #{i + 1}:")
        st.write("Nomor Kamar:", transaction["room_number"])
        st.write("Tanggal Check-in:", transaction["check_in_date"])
        st.write("Tanggal Check-out:", transaction["check_out_date"])
        st.write("-------------")


def calculate_total_revenue():
    st.header("Total Pendapatan")
    total_revenue = 0
    for transaction in transactions:
        total_revenue += (transaction["check_out_date"] - transaction["check_in_date"]).days * 100
    st.write("Total Pendapatan: $", total_revenue)


# Main program
def main():
    st.title("Reservasi Hotel")

    menu_option = st.sidebar.selectbox("Menu Utama", ["Kelola Kamar", "Kelola Transaksi", "Exit"])

    if menu_option == "Kelola Kamar":
        room_menu_option = st.sidebar.selectbox("Kelola Kamar", ["Input Data Kamar", "Status Kamar"])

        if room_menu_option == "Input Data Kamar":
            input_room_data()
        elif room_menu_option == "Status Kamar":
            display_room_status()

    elif menu_option == "Kelola Transaksi":
        transaction_menu_option = st.sidebar.selectbox(
            "Kelola Transaksi",
            ["Input Data Transaksi", "Data Riwayat Transaksi", "Sub Total Reservasi"]
        )

        if transaction_menu_option == "Input Data Transaksi":
            input_transaction_data()
        elif transaction_menu_option == "Data Riwayat Transaksi":
            display_transaction_history()
        elif transaction_menu_option == "Sub Total Reservasi":
            calculate_total_revenue()

    elif menu_option == "Exit":
        st.write("Terima kasih telah menggunakan aplikasi kami. Sampai jumpa lagi!")


if __name__ == "__main__":
    main()

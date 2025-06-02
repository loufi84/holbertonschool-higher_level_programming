#!/usr/bin/python3
'''
This module provides 2 functions to transmit data.
'''
import socket
import json


def start_server(host='127.0.0.1', port=65432):
    '''
    This is the function that start the local server based on port and host.
    It listen to the port and wait data.
    Args:
        host: The adress of the server
        port: The connection port
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = b""
            while True:
                packet = conn.recv(1024)
                if not packet:
                    break
                data += packet
            try:
                received_dict = json.loads(data.decode('utf-8'))
                print("Received dictionary:", received_dict)
            except json.JSONDecodeError:
                print("Failed to decode JSON data")


def send_data(data_dict, host='127.0.0.1', port=65432):
    '''
    The function to send data to the server
    Args:
        data_sict: The serialized data to send
        host: The adress of the server
        port: The port of communication
    '''
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            serialized = json.dumps(data_dict)
            s.sendall(serialized.encode('utf-8'))
    except Exception as e:
        print(f"Connection failed: {e}")

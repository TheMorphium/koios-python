#!/usr/bin/env python
"""
Provides all asset functions
"""
import json
import requests
from .environment import BASE_TIMEOUT, LIMIT_TIMEOUT


def get_asset_list(self, content_range="0-999"):
    """
    Get the list of all native assets (paginated)

    :return: list with all asset list.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            custom_headers = {"Range": str(content_range)}
            asset_list = requests.get(self.ASSET_LIST_URL, headers = custom_headers, timeout=timeout)
            asset_list = json.loads(asset_list.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return asset_list


def get_asset_address_list(self, asset_policy, asset_name, content_range="0-999"):
    """
    Get the list of all addresses holding a given asset.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of all addresses.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            custom_headers = {"Range": str(content_range)}
            info = requests.get(f"{self.ASSET_ADDRESS_LIST_URL}{asset_policy}&_asset_name={asset_name}", \
                headers = custom_headers, timeout=timeout)
            info = json.loads(info.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return info


def get_asset_info(self, asset_policy, asset_name):
    """
    Get the information of an asset including first minting & token registry metadata.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of all asset info.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            info = requests.get(f"{self.ASSET_INFO_URL}{asset_policy}&_asset_name={asset_name}", timeout=timeout)
            info = json.loads(info.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return info


def get_asset_history(self, asset_policy, asset_name):
    """
    Get the mint/burn history of an asset.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of asset mint/burn history.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            history = requests.get(f"{self.ASSET_HISTORY_URL}{asset_policy}&_asset_name={asset_name}", timeout=timeout)
            history = json.loads(history.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return history


def get_asset_policy_info(self, asset_policy):
    """
    Get the information for all assets under the same policy.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :return: list of all mint/burn transactions for an asset
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            info = requests.get(f"{self.ASSET_POLICY_INFO_URL}{asset_policy}", timeout=timeout)
            info = json.loads(info.content)
            break
        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return info


def get_asset_summary(self, asset_policy, asset_name):
    """
    Get the summary of an asset (total transactions exclude minting/total wallets include only
    wallets with asset balance).

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of asset summary information.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            summary = requests.get(f"{self.ASSET_SUMMARY_URL}{asset_policy}&_asset_name={asset_name}", timeout=timeout)
            summary = json.loads(summary.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return summary


def get_asset_txs(self, asset_policy, asset_name, after_block_height=0):
    """
    Get the list of all asset transaction hashes (newest first).

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :param int after_block_height: Block height for specifying time delta, if not data start from 0
    :return: list of all asset hashes transactions.
    :rtype: list.
    """
    timeout = BASE_TIMEOUT

    while True:
        try:
            txs = requests.get(f"{self.ASSET_TXS_URL}{asset_policy}&_asset_name={asset_name}&_after_block_height={after_block_height}", timeout=timeout)
            txs = json.loads(txs.content)
            break

        except requests.exceptions.ReadTimeout as timeout_error:
            print(f"Exception: {timeout_error}")
            if timeout < LIMIT_TIMEOUT:
                timeout= timeout + 10
            else:
                print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                break
            print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")

    return txs
    
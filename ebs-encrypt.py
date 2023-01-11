import boto3
from botocore.exceptions import ClientError
import json

ec2 = boto3.client("ec2")

def ebs_encryption_handler():
  res, reason = get_encryption_status()
  if reason == "Enabled":
    print("EBS Encryption is already enabled")
  elif reason == "Disabled":
    print("EBS Encryption is disabled. Enabling...")
    res, reason = enable_encryption()

def get_encryption_status():
  try:
    status = ec2.get_ebs_encryption_by_default()
    if status['EbsEncryptionByDefault'] == True:
      return (True, "Enabled")
    else:
      return (False, "Disabled")
  except Exception as e:
    return (False, str(e))

def enable_encryption():
  try:
    status = ec2.enable_ebs_encryption_by_default()
    return (True, "Encryption Enabled")
  except Exception as e:
    return (False, str(e))

def disable_encryption():
  try:
    response = ec2.disable_ebs_encryption_by_default()
    return (True, "Encryption Disabled")
  except Exception as e:
    return (False, str(e))

ebs_encryption_handler()

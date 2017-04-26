#!/usr/bin/python

import sys
import boto3
import pprint


def main():
    s3 = boto3.client('s3')
    buckets = sys.argv[1].split()

    for bucket in buckets:
        response = s3.get_bucket_acl(Bucket=bucket)
        pprint.PrettyPrinter(indent=4).pprint(response)


if __name__ == "__main__":
    main()
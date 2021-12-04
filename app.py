#!/usr/bin/env python3

from aws_cdk import core

from cdk_shahab.cdk_shahab_stack import CdkShahabStack


app = core.App()
CdkShahabStack(app, "cdk-shahab")

app.synth()

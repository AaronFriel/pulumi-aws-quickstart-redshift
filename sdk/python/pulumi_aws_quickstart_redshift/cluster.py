# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 db_cluster_identifier: str,
                 db_master_password: pulumi.Input[str],
                 db_master_username: str,
                 db_name: str,
                 db_node_type: str,
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 vpc_id: pulumi.Input[str],
                 additional_security_group_id: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 db_maintenance_window: Optional[str] = None,
                 db_port: Optional[int] = None,
                 enable_event_subscription: Optional[bool] = None,
                 enable_logging: Optional[bool] = None,
                 glue_catalog_database_name: Optional[str] = None,
                 max_concurrent_cluster: Optional[float] = None,
                 notification_email: Optional[str] = None,
                 num_db_nodes: Optional[int] = None,
                 publicly_accessible: Optional[bool] = None,
                 redshift_logging_s3_bucket_name: Optional[str] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param str db_cluster_identifier: The identifier of the Redshift Cluster. Must contain
               only lowercase, alphanumeric characters and hyphens.
        :param pulumi.Input[str] db_master_password: The password that is associated with the master user account
               for the cluster that is being created. Must have at least 8
               characters and no more than 64 characters, and must include 1
               uppercase letter, 1 lowercase letter, 1 number, and 1 symbol
               (excluding / @ \" ').
        :param str db_master_username: The user name that is associated with the master user account
               for the cluster that is being created.
        :param str db_name: The name of the first database to be created when the cluster
               is created.
        :param str db_node_type: The type of node to be provisioned
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The list of subnet IDs in which to deploy the Redshift Cluster
        :param pulumi.Input[str] vpc_id: The VPC with which to create the Redshift Cluster
        :param pulumi.Input[Sequence[pulumi.Input[str]]] additional_security_group_id: An additional list of security group IDs to attach to the redshift cluster
        :param str db_maintenance_window: The maintenance window for the Redshift cluster. e.g 'sat:05:00-sat:05:30'
        :param int db_port: The port number on which the cluster accepts incoming
               connections. Default is 8200
        :param bool enable_event_subscription: Set this parameter to `false` if you want to disable Amazon
               Redshift Cluster and Instance level event subscriptions. You
               might want to disable it if you are testing or running
               continuous integration (CI) processes. Default is `true`.
        :param bool enable_logging: Enables or disables logging to an S3 bucket. To enable logging,
               select True.
        :param str glue_catalog_database_name: The name of your Glue Data Catalog database.
        :param float max_concurrent_cluster: The maximum number of concurrency scaling Redshift
               clusters.
        :param str notification_email: The email notification list that is used to configure an SNS
               topic for sending CloudWatch alarm and event notifications.
        :param int num_db_nodes: The number of compute nodes in the cluster. For multi-node
               clusters, the NumberOfNodes parameter must be greater than
               1.
        :param bool publicly_accessible: Specifies whether Amazon Redshift will be publicly accessible.
               If this option is set to True, the Amazon Redshift cluster will
               be created in a public subnet with security group whitelisting
               to RemoteAccessCIDR.
               If you leave the default option of False, the Amazon Redshift
               cluster will be created in a private subnet with security group
               whitelisting to VPCCIDR.
        :param str redshift_logging_s3_bucket_name: Name for an S3 bucket for logging. An IAM role will be created and
               associated to the Redshift cluster with GET and LIST access to
               this bucket.
        """
        pulumi.set(__self__, "db_cluster_identifier", db_cluster_identifier)
        pulumi.set(__self__, "db_master_password", db_master_password)
        pulumi.set(__self__, "db_master_username", db_master_username)
        pulumi.set(__self__, "db_name", db_name)
        pulumi.set(__self__, "db_node_type", db_node_type)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if additional_security_group_id is not None:
            pulumi.set(__self__, "additional_security_group_id", additional_security_group_id)
        if db_maintenance_window is not None:
            pulumi.set(__self__, "db_maintenance_window", db_maintenance_window)
        if db_port is not None:
            pulumi.set(__self__, "db_port", db_port)
        if enable_event_subscription is not None:
            pulumi.set(__self__, "enable_event_subscription", enable_event_subscription)
        if enable_logging is not None:
            pulumi.set(__self__, "enable_logging", enable_logging)
        if glue_catalog_database_name is not None:
            pulumi.set(__self__, "glue_catalog_database_name", glue_catalog_database_name)
        if max_concurrent_cluster is not None:
            pulumi.set(__self__, "max_concurrent_cluster", max_concurrent_cluster)
        if notification_email is not None:
            pulumi.set(__self__, "notification_email", notification_email)
        if num_db_nodes is not None:
            pulumi.set(__self__, "num_db_nodes", num_db_nodes)
        if publicly_accessible is not None:
            pulumi.set(__self__, "publicly_accessible", publicly_accessible)
        if redshift_logging_s3_bucket_name is not None:
            pulumi.set(__self__, "redshift_logging_s3_bucket_name", redshift_logging_s3_bucket_name)

    @property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> str:
        """
        The identifier of the Redshift Cluster. Must contain
        only lowercase, alphanumeric characters and hyphens.
        """
        return pulumi.get(self, "db_cluster_identifier")

    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: str):
        pulumi.set(self, "db_cluster_identifier", value)

    @property
    @pulumi.getter(name="dbMasterPassword")
    def db_master_password(self) -> pulumi.Input[str]:
        """
        The password that is associated with the master user account
        for the cluster that is being created. Must have at least 8
        characters and no more than 64 characters, and must include 1
        uppercase letter, 1 lowercase letter, 1 number, and 1 symbol
        (excluding / @ \" ').
        """
        return pulumi.get(self, "db_master_password")

    @db_master_password.setter
    def db_master_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "db_master_password", value)

    @property
    @pulumi.getter(name="dbMasterUsername")
    def db_master_username(self) -> str:
        """
        The user name that is associated with the master user account
        for the cluster that is being created.
        """
        return pulumi.get(self, "db_master_username")

    @db_master_username.setter
    def db_master_username(self, value: str):
        pulumi.set(self, "db_master_username", value)

    @property
    @pulumi.getter(name="dbName")
    def db_name(self) -> str:
        """
        The name of the first database to be created when the cluster
        is created.
        """
        return pulumi.get(self, "db_name")

    @db_name.setter
    def db_name(self, value: str):
        pulumi.set(self, "db_name", value)

    @property
    @pulumi.getter(name="dbNodeType")
    def db_node_type(self) -> str:
        """
        The type of node to be provisioned
        """
        return pulumi.get(self, "db_node_type")

    @db_node_type.setter
    def db_node_type(self, value: str):
        pulumi.set(self, "db_node_type", value)

    @property
    @pulumi.getter(name="subnetIDs")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of subnet IDs in which to deploy the Redshift Cluster
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="vpcID")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        The VPC with which to create the Redshift Cluster
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="additionalSecurityGroupID")
    def additional_security_group_id(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An additional list of security group IDs to attach to the redshift cluster
        """
        return pulumi.get(self, "additional_security_group_id")

    @additional_security_group_id.setter
    def additional_security_group_id(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "additional_security_group_id", value)

    @property
    @pulumi.getter(name="dbMaintenanceWindow")
    def db_maintenance_window(self) -> Optional[str]:
        """
        The maintenance window for the Redshift cluster. e.g 'sat:05:00-sat:05:30'
        """
        return pulumi.get(self, "db_maintenance_window")

    @db_maintenance_window.setter
    def db_maintenance_window(self, value: Optional[str]):
        pulumi.set(self, "db_maintenance_window", value)

    @property
    @pulumi.getter(name="dbPort")
    def db_port(self) -> Optional[int]:
        """
        The port number on which the cluster accepts incoming
        connections. Default is 8200
        """
        return pulumi.get(self, "db_port")

    @db_port.setter
    def db_port(self, value: Optional[int]):
        pulumi.set(self, "db_port", value)

    @property
    @pulumi.getter(name="enableEventSubscription")
    def enable_event_subscription(self) -> Optional[bool]:
        """
        Set this parameter to `false` if you want to disable Amazon
        Redshift Cluster and Instance level event subscriptions. You
        might want to disable it if you are testing or running
        continuous integration (CI) processes. Default is `true`.
        """
        return pulumi.get(self, "enable_event_subscription")

    @enable_event_subscription.setter
    def enable_event_subscription(self, value: Optional[bool]):
        pulumi.set(self, "enable_event_subscription", value)

    @property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[bool]:
        """
        Enables or disables logging to an S3 bucket. To enable logging,
        select True.
        """
        return pulumi.get(self, "enable_logging")

    @enable_logging.setter
    def enable_logging(self, value: Optional[bool]):
        pulumi.set(self, "enable_logging", value)

    @property
    @pulumi.getter(name="glueCatalogDatabaseName")
    def glue_catalog_database_name(self) -> Optional[str]:
        """
        The name of your Glue Data Catalog database.
        """
        return pulumi.get(self, "glue_catalog_database_name")

    @glue_catalog_database_name.setter
    def glue_catalog_database_name(self, value: Optional[str]):
        pulumi.set(self, "glue_catalog_database_name", value)

    @property
    @pulumi.getter(name="maxConcurrentCluster")
    def max_concurrent_cluster(self) -> Optional[float]:
        """
        The maximum number of concurrency scaling Redshift
        clusters.
        """
        return pulumi.get(self, "max_concurrent_cluster")

    @max_concurrent_cluster.setter
    def max_concurrent_cluster(self, value: Optional[float]):
        pulumi.set(self, "max_concurrent_cluster", value)

    @property
    @pulumi.getter(name="notificationEmail")
    def notification_email(self) -> Optional[str]:
        """
        The email notification list that is used to configure an SNS
        topic for sending CloudWatch alarm and event notifications.
        """
        return pulumi.get(self, "notification_email")

    @notification_email.setter
    def notification_email(self, value: Optional[str]):
        pulumi.set(self, "notification_email", value)

    @property
    @pulumi.getter(name="numDbNodes")
    def num_db_nodes(self) -> Optional[int]:
        """
        The number of compute nodes in the cluster. For multi-node
        clusters, the NumberOfNodes parameter must be greater than
        1.
        """
        return pulumi.get(self, "num_db_nodes")

    @num_db_nodes.setter
    def num_db_nodes(self, value: Optional[int]):
        pulumi.set(self, "num_db_nodes", value)

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[bool]:
        """
        Specifies whether Amazon Redshift will be publicly accessible.
        If this option is set to True, the Amazon Redshift cluster will
        be created in a public subnet with security group whitelisting
        to RemoteAccessCIDR.
        If you leave the default option of False, the Amazon Redshift
        cluster will be created in a private subnet with security group
        whitelisting to VPCCIDR.
        """
        return pulumi.get(self, "publicly_accessible")

    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[bool]):
        pulumi.set(self, "publicly_accessible", value)

    @property
    @pulumi.getter(name="redshiftLoggingS3BucketName")
    def redshift_logging_s3_bucket_name(self) -> Optional[str]:
        """
        Name for an S3 bucket for logging. An IAM role will be created and
        associated to the Redshift cluster with GET and LIST access to
        this bucket.
        """
        return pulumi.get(self, "redshift_logging_s3_bucket_name")

    @redshift_logging_s3_bucket_name.setter
    def redshift_logging_s3_bucket_name(self, value: Optional[str]):
        pulumi.set(self, "redshift_logging_s3_bucket_name", value)


class Cluster(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_security_group_id: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 db_cluster_identifier: Optional[str] = None,
                 db_maintenance_window: Optional[str] = None,
                 db_master_password: Optional[pulumi.Input[str]] = None,
                 db_master_username: Optional[str] = None,
                 db_name: Optional[str] = None,
                 db_node_type: Optional[str] = None,
                 db_port: Optional[int] = None,
                 enable_event_subscription: Optional[bool] = None,
                 enable_logging: Optional[bool] = None,
                 glue_catalog_database_name: Optional[str] = None,
                 max_concurrent_cluster: Optional[float] = None,
                 notification_email: Optional[str] = None,
                 num_db_nodes: Optional[int] = None,
                 publicly_accessible: Optional[bool] = None,
                 redshift_logging_s3_bucket_name: Optional[str] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] additional_security_group_id: An additional list of security group IDs to attach to the redshift cluster
        :param str db_cluster_identifier: The identifier of the Redshift Cluster. Must contain
               only lowercase, alphanumeric characters and hyphens.
        :param str db_maintenance_window: The maintenance window for the Redshift cluster. e.g 'sat:05:00-sat:05:30'
        :param pulumi.Input[str] db_master_password: The password that is associated with the master user account
               for the cluster that is being created. Must have at least 8
               characters and no more than 64 characters, and must include 1
               uppercase letter, 1 lowercase letter, 1 number, and 1 symbol
               (excluding / @ \" ').
        :param str db_master_username: The user name that is associated with the master user account
               for the cluster that is being created.
        :param str db_name: The name of the first database to be created when the cluster
               is created.
        :param str db_node_type: The type of node to be provisioned
        :param int db_port: The port number on which the cluster accepts incoming
               connections. Default is 8200
        :param bool enable_event_subscription: Set this parameter to `false` if you want to disable Amazon
               Redshift Cluster and Instance level event subscriptions. You
               might want to disable it if you are testing or running
               continuous integration (CI) processes. Default is `true`.
        :param bool enable_logging: Enables or disables logging to an S3 bucket. To enable logging,
               select True.
        :param str glue_catalog_database_name: The name of your Glue Data Catalog database.
        :param float max_concurrent_cluster: The maximum number of concurrency scaling Redshift
               clusters.
        :param str notification_email: The email notification list that is used to configure an SNS
               topic for sending CloudWatch alarm and event notifications.
        :param int num_db_nodes: The number of compute nodes in the cluster. For multi-node
               clusters, the NumberOfNodes parameter must be greater than
               1.
        :param bool publicly_accessible: Specifies whether Amazon Redshift will be publicly accessible.
               If this option is set to True, the Amazon Redshift cluster will
               be created in a public subnet with security group whitelisting
               to RemoteAccessCIDR.
               If you leave the default option of False, the Amazon Redshift
               cluster will be created in a private subnet with security group
               whitelisting to VPCCIDR.
        :param str redshift_logging_s3_bucket_name: Name for an S3 bucket for logging. An IAM role will be created and
               associated to the Redshift cluster with GET and LIST access to
               this bucket.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The list of subnet IDs in which to deploy the Redshift Cluster
        :param pulumi.Input[str] vpc_id: The VPC with which to create the Redshift Cluster
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_security_group_id: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 db_cluster_identifier: Optional[str] = None,
                 db_maintenance_window: Optional[str] = None,
                 db_master_password: Optional[pulumi.Input[str]] = None,
                 db_master_username: Optional[str] = None,
                 db_name: Optional[str] = None,
                 db_node_type: Optional[str] = None,
                 db_port: Optional[int] = None,
                 enable_event_subscription: Optional[bool] = None,
                 enable_logging: Optional[bool] = None,
                 glue_catalog_database_name: Optional[str] = None,
                 max_concurrent_cluster: Optional[float] = None,
                 notification_email: Optional[str] = None,
                 num_db_nodes: Optional[int] = None,
                 publicly_accessible: Optional[bool] = None,
                 redshift_logging_s3_bucket_name: Optional[str] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            __props__.__dict__["additional_security_group_id"] = additional_security_group_id
            if db_cluster_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'db_cluster_identifier'")
            __props__.__dict__["db_cluster_identifier"] = db_cluster_identifier
            __props__.__dict__["db_maintenance_window"] = db_maintenance_window
            if db_master_password is None and not opts.urn:
                raise TypeError("Missing required property 'db_master_password'")
            __props__.__dict__["db_master_password"] = None if db_master_password is None else pulumi.Output.secret(db_master_password)
            if db_master_username is None and not opts.urn:
                raise TypeError("Missing required property 'db_master_username'")
            __props__.__dict__["db_master_username"] = db_master_username
            if db_name is None and not opts.urn:
                raise TypeError("Missing required property 'db_name'")
            __props__.__dict__["db_name"] = db_name
            if db_node_type is None and not opts.urn:
                raise TypeError("Missing required property 'db_node_type'")
            __props__.__dict__["db_node_type"] = db_node_type
            __props__.__dict__["db_port"] = db_port
            __props__.__dict__["enable_event_subscription"] = enable_event_subscription
            __props__.__dict__["enable_logging"] = enable_logging
            __props__.__dict__["glue_catalog_database_name"] = glue_catalog_database_name
            __props__.__dict__["max_concurrent_cluster"] = max_concurrent_cluster
            __props__.__dict__["notification_email"] = notification_email
            __props__.__dict__["num_db_nodes"] = num_db_nodes
            __props__.__dict__["publicly_accessible"] = publicly_accessible
            __props__.__dict__["redshift_logging_s3_bucket_name"] = redshift_logging_s3_bucket_name
            if subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_ids'")
            __props__.__dict__["subnet_ids"] = subnet_ids
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
        super(Cluster, __self__).__init__(
            'aws-quickstart-redshift:index:Cluster',
            resource_name,
            __props__,
            opts,
            remote=True)


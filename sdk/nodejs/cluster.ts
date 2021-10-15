// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Cluster extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'aws-quickstart-redshift:index:Cluster';

    /**
     * Returns true if the given object is an instance of Cluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Cluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Cluster.__pulumiType;
    }


    /**
     * Create a Cluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ClusterArgs, opts?: pulumi.ComponentResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.dbClusterIdentifier === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dbClusterIdentifier'");
            }
            if ((!args || args.dbMasterPassword === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dbMasterPassword'");
            }
            if ((!args || args.dbMasterUsername === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dbMasterUsername'");
            }
            if ((!args || args.dbName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dbName'");
            }
            if ((!args || args.dbNodeType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dbNodeType'");
            }
            if ((!args || args.subnetIDs === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnetIDs'");
            }
            if ((!args || args.vpcID === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcID'");
            }
            inputs["additionalSecurityGroupID"] = args ? args.additionalSecurityGroupID : undefined;
            inputs["dbClusterIdentifier"] = args ? args.dbClusterIdentifier : undefined;
            inputs["dbMaintenanceWindow"] = args ? args.dbMaintenanceWindow : undefined;
            inputs["dbMasterPassword"] = args?.dbMasterPassword ? pulumi.secret(args.dbMasterPassword) : undefined;
            inputs["dbMasterUsername"] = args ? args.dbMasterUsername : undefined;
            inputs["dbName"] = args ? args.dbName : undefined;
            inputs["dbNodeType"] = args ? args.dbNodeType : undefined;
            inputs["dbPort"] = args ? args.dbPort : undefined;
            inputs["enableEventSubscription"] = args ? args.enableEventSubscription : undefined;
            inputs["enableLogging"] = args ? args.enableLogging : undefined;
            inputs["glueCatalogDatabaseName"] = args ? args.glueCatalogDatabaseName : undefined;
            inputs["maxConcurrentCluster"] = args ? args.maxConcurrentCluster : undefined;
            inputs["notificationEmail"] = args ? args.notificationEmail : undefined;
            inputs["numDbNodes"] = args ? args.numDbNodes : undefined;
            inputs["publiclyAccessible"] = args ? args.publiclyAccessible : undefined;
            inputs["redshiftLoggingS3BucketName"] = args ? args.redshiftLoggingS3BucketName : undefined;
            inputs["subnetIDs"] = args ? args.subnetIDs : undefined;
            inputs["vpcID"] = args ? args.vpcID : undefined;
        } else {
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Cluster.__pulumiType, name, inputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a Cluster resource.
 */
export interface ClusterArgs {
    /**
     * An additional list of security group IDs to attach to the redshift cluster
     */
    additionalSecurityGroupID?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The identifier of the Redshift Cluster. Must contain
     * only lowercase, alphanumeric characters and hyphens.
     */
    dbClusterIdentifier: string;
    /**
     * The maintenance window for the Redshift cluster. e.g 'sat:05:00-sat:05:30'
     */
    dbMaintenanceWindow?: string;
    /**
     * The password that is associated with the master user account
     * for the cluster that is being created. Must have at least 8
     * characters and no more than 64 characters, and must include 1
     * uppercase letter, 1 lowercase letter, 1 number, and 1 symbol
     * (excluding / @ \" ').
     */
    dbMasterPassword: pulumi.Input<string>;
    /**
     * The user name that is associated with the master user account
     * for the cluster that is being created.
     */
    dbMasterUsername: string;
    /**
     * The name of the first database to be created when the cluster
     * is created.
     */
    dbName: string;
    /**
     * The type of node to be provisioned
     */
    dbNodeType: string;
    /**
     * The port number on which the cluster accepts incoming
     * connections. Default is 8200
     */
    dbPort?: number;
    /**
     * Set this parameter to `false` if you want to disable Amazon
     * Redshift Cluster and Instance level event subscriptions. You
     * might want to disable it if you are testing or running
     * continuous integration (CI) processes. Default is `true`.
     */
    enableEventSubscription?: boolean;
    /**
     * Enables or disables logging to an S3 bucket. To enable logging,
     * select True.
     */
    enableLogging?: boolean;
    /**
     * The name of your Glue Data Catalog database.
     */
    glueCatalogDatabaseName?: string;
    /**
     * The maximum number of concurrency scaling Redshift
     * clusters.
     */
    maxConcurrentCluster?: number;
    /**
     * The email notification list that is used to configure an SNS
     * topic for sending CloudWatch alarm and event notifications.
     */
    notificationEmail?: string;
    /**
     * The number of compute nodes in the cluster. For multi-node
     * clusters, the NumberOfNodes parameter must be greater than
     * 1.
     */
    numDbNodes?: number;
    /**
     * Specifies whether Amazon Redshift will be publicly accessible.
     * If this option is set to True, the Amazon Redshift cluster will
     * be created in a public subnet with security group whitelisting
     * to RemoteAccessCIDR.
     * If you leave the default option of False, the Amazon Redshift
     * cluster will be created in a private subnet with security group
     * whitelisting to VPCCIDR.
     */
    publiclyAccessible?: boolean;
    /**
     * Name for an S3 bucket for logging. An IAM role will be created and
     * associated to the Redshift cluster with GET and LIST access to
     * this bucket.
     */
    redshiftLoggingS3BucketName?: string;
    /**
     * The list of subnet IDs in which to deploy the Redshift Cluster
     */
    subnetIDs: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The VPC with which to create the Redshift Cluster
     */
    vpcID: pulumi.Input<string>;
}

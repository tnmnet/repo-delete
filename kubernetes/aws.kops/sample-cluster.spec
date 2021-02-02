metadata:
  creationTimestamp: "2020-06-30T10:03:58Z"
  name: cluster.dops-lab.com
spec:
  api:
    dns: {}
  authorization:
    rbac: {}
  channel: stable
  cloudProvider: aws
  clusterDNSDomain: cluster.local
  configBase: s3://devops-demo-kops-state-store/cluster.dops-lab.com
  configStore: s3://devops-demo-kops-state-store/cluster.dops-lab.com
  dnsZone: Z2MP9F6HI9RYO3
  docker:
    ipMasq: false
    ipTables: false
    logDriver: json-file
    logLevel: warn
    logOpt:
    - max-size=10m
    - max-file=5
    storage: overlay2,overlay,aufs
    version: 19.03.4
  etcdClusters:
  - backups:
      backupStore: s3://devops-demo-kops-state-store/cluster.dops-lab.com/backups/etcd/main
    cpuRequest: 200m
    enableEtcdTLS: true
    enableTLSAuth: true
    etcdMembers:
    - instanceGroup: master-us-east-2b
      name: b
    manager: {}
    memoryRequest: 100Mi
    name: main
    provider: Manager
    version: 3.4.3
  - backups:
      backupStore: s3://devops-demo-kops-state-store/cluster.dops-lab.com/backups/etcd/events
    cpuRequest: 100m
    enableEtcdTLS: true
    enableTLSAuth: true
    etcdMembers:
    - instanceGroup: master-us-east-2b
      name: b
    manager: {}
    memoryRequest: 100Mi
    name: events
    provider: Manager
    version: 3.4.3
  iam:
    allowContainerRegistry: true
    legacy: false
  keyStore: s3://devops-demo-kops-state-store/cluster.dops-lab.com/pki
  kubeAPIServer:
    allowPrivileged: true
    anonymousAuth: false
    apiServerCount: 1
    authorizationMode: RBAC
    bindAddress: 0.0.0.0
    cloudProvider: aws
    enableAdmissionPlugins:
    - NamespaceLifecycle
    - LimitRanger
    - ServiceAccount
    - PersistentVolumeLabel
    - DefaultStorageClass
    - DefaultTolerationSeconds
    - MutatingAdmissionWebhook
    - ValidatingAdmissionWebhook
    - NodeRestriction
    - ResourceQuota
    etcdServers:
    - http://127.0.0.1:4001
    etcdServersOverrides:
    - /events#http://127.0.0.1:4002
    image: k8s.gcr.io/kube-apiserver:v1.17.6
    insecureBindAddress: 127.0.0.1
    kubeletPreferredAddressTypes:
    - InternalIP
    - Hostname
    - ExternalIP
    logLevel: 2
    requestheaderAllowedNames:
    - aggregator
    requestheaderExtraHeaderPrefixes:
    - X-Remote-Extra-
    requestheaderGroupHeaders:
    - X-Remote-Group
    requestheaderUsernameHeaders:
    - X-Remote-User
    securePort: 443
    serviceClusterIPRange: 100.64.0.0/13
    storageBackend: etcd3
  kubeControllerManager:
    allocateNodeCIDRs: true
    attachDetachReconcileSyncPeriod: 1m0s
    cloudProvider: aws
    clusterCIDR: 100.96.0.0/11
    clusterName: cluster.dops-lab.com
    configureCloudRoutes: true
    image: k8s.gcr.io/kube-controller-manager:v1.17.6
    leaderElection:
      leaderElect: true
    logLevel: 2
    useServiceAccountCredentials: true
  kubeDNS:
    cacheMaxConcurrent: 150
    cacheMaxSize: 1000
    cpuRequest: 100m
    domain: cluster.local
    memoryLimit: 170Mi
    memoryRequest: 70Mi
    replicas: 2
    serverIP: 100.64.0.10
  kubeProxy:
    clusterCIDR: 100.96.0.0/11
    cpuRequest: 100m
    hostnameOverride: '@aws'
    image: k8s.gcr.io/kube-proxy:v1.17.6
    logLevel: 2
  kubeScheduler:
    image: k8s.gcr.io/kube-scheduler:v1.17.6
    leaderElection:
      leaderElect: true
    logLevel: 2
  kubelet:
    anonymousAuth: false
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    networkPluginMTU: 9001
    networkPluginName: kubenet
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: k8s.gcr.io/pause-amd64:3.0
    podManifestPath: /etc/kubernetes/manifests
  kubernetesApiAccess:
  - 0.0.0.0/0
  kubernetesVersion: 1.17.6
  masterInternalName: api.internal.cluster.dops-lab.com
  masterKubelet:
    anonymousAuth: false
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    networkPluginMTU: 9001
    networkPluginName: kubenet
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: k8s.gcr.io/pause-amd64:3.0
    podManifestPath: /etc/kubernetes/manifests
    registerSchedulable: false
  masterPublicName: api.cluster.dops-lab.com
  networkCIDR: 172.20.0.0/16
  networking:
    kubenet: {}
  nonMasqueradeCIDR: 100.64.0.0/10
  secretStore: s3://devops-demo-kops-state-store/cluster.dops-lab.com/secrets
  serviceClusterIPRange: 100.64.0.0/13
  sshAccess:
  - 0.0.0.0/0
  subnets:
  - cidr: 172.20.32.0/19
    name: us-east-2b
    type: Public
    zone: us-east-2b
  topology:
    dns:
      type: Public
    masters: public
    nodes: public

<h1 align="center">
  <br>
  <a href="https://phoenixnap.com/bare-metal-cloud"><img src="https://user-images.githubusercontent.com/78744488/109779287-16da8600-7c06-11eb-81a1-97bf44983d33.png" alt="phoenixnap Bare Metal Cloud" width="300"></a>
  <br>
  Bare Metal Cloud Drive Encryption Using EMP
  <br>
</h1>

<p align="center">
Automatically mount an encrypted drive on Bare Metal Cloud. This collection uses the phoenixNAP Encryption Management Platform (EMP) as a key storage and PyKMIP to transfer certificates for maximum token security.

<p align="center">
  <a href="https://phoenixnap.com/bare-metal-cloud">Bare Metal Cloud</a> •
  <a href="https://phoenixnap.com/security/encryption-management-platform">Encryption Management Platform</a> •
  <a href="https://developers.phoenixnap.com/">Developers Portal</a> •
  <a href="http://phoenixnap.com/kb">Knowledge Base</a> •
  <a href="https://developers.phoenixnap.com/support">Support</a>
</p>

## Requirements

- [Bare Metal Cloud](https://phoenixnap.com/kb/bare-metal-cloud-portal-quick-start-guide) account
- [EMP](https://phoenixnap.com/kb/provision-secure-tokens-secrets-emp) account
- Python 3 (versions 3.6 and higher)
  - Python **PyKMIP** package
- Cryptsetup
```
sudo apt install cryptsetup-bin
```
- luksFormat

## Creating a Bare Metal Cloud account

1. Go to the [Bare Metal Cloud signup page](https://support.phoenixnap.com/wap-jpost3/bmcSignup).
2. Follow the prompts to set up your account.
3. Use your credentials to [log in to Bare Metal Cloud portal](https://bmc.phoenixnap.com).

:arrow_forward: **Video tutorial:** [How to Create a Bare Metal Cloud Account](https://www.youtube.com/watch?v=RLRQOisEB-k)
<br>

:arrow_forward: **Video tutorial:** [Introduction to Bare Metal Cloud](https://www.youtube.com/watch?v=8TLsqgLDMN4)

## Creating an EMP account

1. Go to the [EMP signup page](https://emp.phoenixnap.com/#/?signup).
2. Follow the prompts to set up your account.
3. Use your credentials to [log in to EMP portal](https://emp.phoenixnap.com/#/).

## Pre-Setup EMP

[Provision and secure tokens](https://phoenixnap.com/kb/provision-secure-tokens-secrets-emp) using the phoenixNAP EMP platform.

1. Create **Group**.
2. Add **New App** to the group. 
3. Copy the **UUID** of the App.
4. [SSH into the BMC](https://phoenixnap.com/kb/bmc-remote-console) server and provide the identity file. For example:
```
ssh -i .ssh/id_rsa ubuntu@123.456.789
```
5. In the terminal, generate a private key:
``` 
openssl genrsa -out <key name>.key
```
6. Generate the certificate using the key. Set the **Common Name** as the App **UUID**:
```
openssl req -new -x509 -key <key name>.key -out <certificate name>.cert -days <number of days>
```
7. Change App authentication to **Certificate** and upload generated Certificate to the App.

## Installing PyKMIP

1. Update and upgrade the system:
```
sudo apt update && sudo apt upgrade
```
2. Install pip for Python 3 with the following command:
```
sudo apt install python3-pip
```
3. Upgrade pip:
```
pip3 install --upgrade pip
```
4. Install the PyKMIP module by running:
```
sudo -H pip3 install pykmip
```

## Security Object

Use the **`pykimp.conf`** file as a configuration template for PyKMIP and add the paths to the security objects. Run the **`generate_key.py`** script to create a security object in EMP. Copy the UUID of the security object and add it to the **`key.py`** script to fetch the key automatically.

## Encrypt the Device Using LUKS and CryptSetup

1. Create an encrypted file container using the dd command:
```
dd of=secretfs bs=1G count=0 seek=2
```
2. Change the container permission to 600 using the chmod command:
```
sudo chmod 600 secretfs
```
3. Attach the file container to a loop device with the losetup command:
```
sudo losetup /dev/loop101 secretfs
```
4. Using the key.py script, format the loop device using cryptsetup and luksFormat:
```
python3 key.py | sudo cryptsetup -y luksFormat /dev/loop101
```
This command encrypts the device using LUKS encryption with the key stored in EMP.

5. Open the encrypted file container on the loop device using the key:
```
python3 key.py | sudo cryptsetup luksOpen /dev/loop101 secretfs
```

## Mount Encrypted Filesystem

1. Format the disk using the mkfs command:
```
sudo mkfs.ext4 /dev/mapper/secretfs
```
2. Make a mount point for the file system:
```
sudo mkdir /mnt/encrypted
```
3. Mount the disk:
```
sudo mount /dev/mapper/secretfs /mnt/encrypted
```
4. Check that the device mounted:
```
df | grep secretfs
```

## Automount Script

Create a service in **`/etc/init.d`** with the contents of the **`automount`** file. Make the service executable, update service information and reboot. The service automatically starts on reboot. Check status of the servie after reboot with:

```
systemctl status automount
```

In case of compromise, revoke security object from EMP and the device doesn't automatically unlock and mount on the next restart. In case of connection error, the service retries to connect.

For a comprehensive tutorial, visit our KB: [BMC Drive Encryption Using EMP](https://phoenixnap.com/kb/how-to-set-up-bmc-drive-encryption-using-emp)

## Bare Metal Cloud community

Become part of the Bare Metal Cloud community to get updates on new features, help us improve the platform, and engage with developers and other users.

- Follow [@phoenixNAP on Twitter](https://twitter.com/phoenixnap)
- Join the [official Slack channel](https://phoenixnap.slack.com)
- Sign up for our [Developers Monthly newsletter](https://phoenixnap.com/developers-monthly-newsletter)

### Resources

- [Product page](https://phoenixnap.com/bare-metal-cloud)
- [Instance pricing](https://phoenixnap.com/bare-metal-cloud/instances)
- [YouTube tutorials](https://www.youtube.com/watch?v=8TLsqgLDMN4&list=PLWcrQnFWd54WwkHM0oPpR1BrAhxlsy1Rc&ab_channel=PhoenixNAPGlobalITServices)
- [Developers Portal](https://developers.phoenixnap.com)
- [Knowledge Base](https://phoenixnap.com/kb)
- [Blog](https:/phoenixnap.com/blog)

### Documentation

- [API documentation](https://developers.phoenixnap.com/docs/bmc/1/overview)

### Contact phoenixNAP

Get in touch with us if you have questions or need help with Bare Metal Cloud.

<p align="left">
  <a href="https://twitter.com/phoenixNAP">Twitter</a> •
  <a href="https://www.facebook.com/phoenixnap">Facebook</a> •
  <a href="https://www.linkedin.com/company/phoenix-nap">LinkedIn</a> •
  <a href="https://www.instagram.com/phoenixnap">Instagram</a> •
  <a href="https://www.youtube.com/user/PhoenixNAPdatacenter">YouTube</a> •
  <a href="https://developers.phoenixnap.com/support">Email</a> 
</p>

<p align="center">
  <br>
  <a href="https://phoenixnap.com/bare-metal-cloud"><img src="https://user-images.githubusercontent.com/81640346/115243282-0c773b80-a123-11eb-9de7-59e3934a5712.jpg" alt="phoenixnap Bare Metal Cloud"></a>
</p>

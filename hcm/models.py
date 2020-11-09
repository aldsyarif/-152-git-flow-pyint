# from django.db import models

# # Create your models here.


# class Users(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=255)
#     email_verified_at = models.DateTimeField
#     remember_token = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     nik = models.IntegerField(null=False)
#     posision = models.CharField(max_length=45)
#     unit_level_1 = models.CharField(max_length=255)
#     unit = models.CharField(max_length=255)
#     band_posisi = models.CharField(max_length=45)
#     divisi = models.CharField(max_length=50)
#     direktorat = models.CharField(max_length=50)
#     status = models.CharField(max_length=45)
#     phone = models.CharField(max_length=45)
#     atasan_nik = models.CharField(max_length=45)
#     atasan_atasan_nik = models.CharField(max_length=45)
#     bawahan = models.TextField
#     ldap_update = models.IntegerField(null=False)
#     picture = models.TextField
#     is_firts_login = models.IntegerField(null=False)
#     is_change_agent = models.IntegerField(null=False)

#     class Meta:
#         db_table = "users"

#     def __str__(self):
#         return self.name


# class Okr(models.Model):
#     indicator = models.CharField(max_length=255)
#     objective = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=15)
#     start_date = models.DateField
#     rate = models.DecimalField(max_digits=10, decimal_places=2)
#     type = models.CharField(max_length=45)
#     id_created = models.ForeignKey(Users, on_delete=models.CASCADE)
#     is_active = models.IntegerField(null=False)

#     class Meta:
#         db_table = "okr"

#     def __str__(self):
#         return self.name


# class KeyResult(models.Model):
#     id_okr = models.ForeignKey(Okr, on_delete=models.CASCADE)
#     id_key_result = models.IntegerField(null=False)
#     key_result = models.CharField(max_length=255)
#     due_date = models.DateField
#     status = models.IntegerField(null=False)
#     rate = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "key_result"

#     def __str__(self):
#         return self.name


# class OkrOutput(models.Model):
#     id_okr = models.ForeignKey(Okr, on_delete=models.CASCADE)
#     output = models.TextField
#     duedate = models.DateField
#     status = models.IntegerField(null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "okr_output"

#     def __str__(self):
#         return self.name

import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin, User
from django.conf import settings


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser,
                     **extra_fields):
        if not email:
            raise ValueError('The given username must be set')
        # username = self.normalize_username(username)
        user = self.model(email=email,
                          is_superuser=is_superuser,
                          last_login=timezone.now(),
                          date_joined=timezone.now(),
                          **extra_fields)

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class OpsCustomuser(AbstractBaseUser, PermissionsMixin):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    fullname = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(
        unique=True, max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=254)
    nrp = models.BigIntegerField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    is_operator = models.BooleanField()
    is_commander = models.BooleanField()
    is_reset_pass = models.BooleanField()
    is_api = models.BooleanField()
    organization = models.ForeignKey(
        'OpsOrganization', models.DO_NOTHING, verbose_name='Satuan', blank=True, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        managed = False
        db_table = 'ops_customuser'


class OpsOrganization(models.Model):
    name = models.CharField(unique=True, max_length=200)
    level = models.IntegerField(blank=True, null=True)
    priority_type = models.CharField(max_length=20, blank=True, null=True)
    combat_type = models.CharField(max_length=20, blank=True, null=True)
    is_induk = models.BooleanField(blank=True, null=True)
    is_rahwan = models.BooleanField(blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    img_path = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    leader = models.CharField(max_length=200, blank=True, null=True)
    leader_pangkat = models.CharField(max_length=500, blank=True, null=True)
    leader_jabatan = models.CharField(max_length=500, blank=True, null=True)
    vice_leader = models.CharField(max_length=200, blank=True, null=True)
    vice_leader_pangkat = models.CharField(
        max_length=500, blank=True, null=True)
    vice_leader_jabatan = models.CharField(
        max_length=500, blank=True, null=True)
    tipe = models.IntegerField(blank=True, null=True)
    is_balakpus = models.BooleanField()
    is_komoditas = models.BooleanField()
    leader_phone = models.CharField(max_length=20, blank=True, null=True)
    is_kantor = models.BooleanField()
    kop_name = models.CharField(max_length=200, blank=True, null=True)
    parent_kop_name = models.CharField(max_length=200, blank=True, null=True)
    level_0 = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='child_0', null=True, blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='child', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ops_organization'

    class Personil(models.Model):
        nrp = models.BigIntegerField(unique=True)
        name = models.CharField(max_length=200, unique=False)
        rank = models.CharField(max_length=500)
        job = models.CharField(max_length=500)
        organization = models.ForeignKey(
            'OpsOrganization', on_delete=models.CASCADE, null=True, blank=True)
        img_path = models.ImageField(
            upload_to='personil', null=True, blank=True)
        phone = models.CharField(max_length=20, null=True, blank=True)

        def __unicode__(self):
            return self.name


class SiapsatUrutanPelaporanEkko(models.Model):
    id = models.BigIntegerField(primary_key=True)
    year = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    urutan = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    level_0 = models.ForeignKey(
        'self', models.DO_NOTHING, related_name='child_0', blank=True, null=True)
    organization = models.ForeignKey(OpsOrganization, models.DO_NOTHING)
    parent = models.ForeignKey(
        'self', models.DO_NOTHING, related_name='child', blank=True, null=True)
    user = models.ForeignKey(OpsCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'siapsat_urutan_pelaporan_ekko'

# Create your models here.


class NilaiSenapan(models.Model):
    # name = models.CharField(max_length=200, unique=False, null=True, blank=True)
    # pangkat = models.CharField(max_length=50, null=True, blank=True)
    # job = models.CharField(max_length=50)
    nrp = models.ForeignKey('Personil', on_delete=models.CASCADE,
                            related_name='nrp_senapan', null=True, blank=True)
    # jabatan = models.CharField(max_length=50, null=True, blank=True)
    sikap = models.CharField(max_length=50, null=True, blank=True)
    jml_mu = models.CharField(max_length=20, null=True, blank=True)
    hit_10 = models.IntegerField(null=True, blank=True)
    hit_9 = models.IntegerField(null=True, blank=True)
    hit_8 = models.IntegerField(null=True, blank=True)
    hit_7 = models.IntegerField(null=True, blank=True)
    hit_6 = models.IntegerField(null=True, blank=True)
    hit_5 = models.IntegerField(null=True, blank=True)
    hit_4 = models.IntegerField(null=True, blank=True)
    hit_3 = models.IntegerField(null=True, blank=True)
    hit_2 = models.IntegerField(null=True, blank=True)
    hit_1 = models.IntegerField(null=True, blank=True)
    jp = models.IntegerField(null=True, blank=True)
    jn = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    average = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    prosentase = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    information = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(
        OpsCustomuser, on_delete=models.CASCADE, related_name='creator_senapan', null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    periode = models.CharField(max_length=20, blank=True, null=True)
    is_latest = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    rank = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    organization = models.ForeignKey(
        OpsOrganization, on_delete=models.CASCADE, null=True, blank=True)


class RekapSenapan(models.Model):
    level0 = models.ForeignKey(OpsOrganization, on_delete=models.CASCADE,
                               related_name='level0_senapan', null=True, blank=True)
    lulus = models.IntegerField(null=True, blank=True)
    fail = models.IntegerField(null=True, blank=True)
    nihil = models.IntegerField(null=True, blank=True)
    prosentase = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    periode = models.CharField(max_length=20, blank=True, null=True)
    year = models.IntegerField(null=True, blank=True)
    upload_at = models.DateTimeField(null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)


def path_and_rename(instance, filename):
    upload_to = 'excel'
    ext = filename.split('.')[-1]

    # get filename
    filename = '{}.{}'.format(instance.file_name, ext)
    file = os.path.exists(os.path.join(
        settings.MEDIA_ROOT, ("excel/" + filename)))
    if file:
        os.remove(os.path.join(settings.MEDIA_ROOT, ("excel/" + filename)))

    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Excel_Upload(models.Model):
    triwulan = models.CharField(max_length=20, blank=True, null=True)
    year = models.IntegerField(null=True, blank=True)
    excel_path = models.FileField(
        upload_to=path_and_rename, null=True, blank=True)
    file_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    organization = models.ForeignKey(
        OpsOrganization, on_delete=models.CASCADE, null=True, blank=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.file_name


class RekapPistol(models.Model):
    level0 = models.ForeignKey(OpsOrganization, on_delete=models.CASCADE,
                               related_name='level0_pistol', null=True, blank=True)
    lulus = models.IntegerField(null=True, blank=True)
    fail = models.IntegerField(null=True, blank=True)
    nihil = models.IntegerField(null=True, blank=True)
    prosentase = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    periode = models.CharField(max_length=20, blank=True, null=True)
    year = models.IntegerField(null=True, blank=True)
    upload_at = models.DateTimeField(null=True, blank=True)


class NilaiGarjas(models.Model):
    nrp = models.ForeignKey('Personil', on_delete=models.CASCADE,
                            related_name='nrp_garjas', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    height = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    body_classification = models.CharField(max_length=5, null=True, blank=True)
    waktu_lari = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    nilai_lari = models.IntegerField(null=True, blank=True)
    pull_ups = models.IntegerField(null=True, blank=True)
    nilai_pull_ups = models.IntegerField(null=True, blank=True)
    sit_ups = models.IntegerField(null=True, blank=True)
    nilai_sit_ups = models.IntegerField(null=True, blank=True)
    push_ups = models.IntegerField(null=True, blank=True)
    nilai_push_ups = models.IntegerField(null=True, blank=True)
    shuttle_run = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    nilai_shuttle_run = models.IntegerField(null=True, blank=True)
    renang = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    renang_l = models.CharField(max_length=5, null=True, blank=True)
    renang_tl = models.CharField(max_length=5, null=True, blank=True)
    average_b = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    total_average = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    final_classification = models.CharField(
        max_length=5, null=True, blank=True)
    information = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(
        OpsCustomuser, on_delete=models.CASCADE, related_name='creator_garjas', null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    periode = models.CharField(max_length=20, blank=True, null=True)
    is_latest = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    rank = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    organization = models.ForeignKey(
        OpsOrganization, on_delete=models.CASCADE, null=True, blank=True)
    dada = models.IntegerField(null=True, blank=True)
    pok_umur = models.CharField(max_length=10, null=True, blank=True)
    jenis_kelamin = models.CharField(max_length=1, null=True, blank=True)
    putaran_lari = models.IntegerField(null=True, blank=True)
    jarak_henti_lari = models.IntegerField(null=True, blank=True)
    jarak_lari = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    gaya_renang = models.CharField(max_length=10, null=True, blank=True)


class RekapGarjas(models.Model):
    level0 = models.ForeignKey(OpsOrganization, on_delete=models.CASCADE,
                               related_name='level0_garjas', null=True, blank=True)
    lulus = models.IntegerField(null=True, blank=True)
    fail = models.IntegerField(null=True, blank=True)
    nihil = models.IntegerField(null=True, blank=True)
    prosentase = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    periode = models.CharField(max_length=20, blank=True, null=True)
    year = models.IntegerField(null=True, blank=True)
    upload_at = models.DateTimeField(null=True, blank=True)


class RekapBDM(models.Model):
    level0 = models.ForeignKey(OpsOrganization, on_delete=models.CASCADE,
                               related_name='level0_bdm', null=True, blank=True)
    putih = models.IntegerField(null=True, blank=True)
    kuning = models.IntegerField(null=True, blank=True)
    hijau = models.IntegerField(null=True, blank=True)
    biru = models.IntegerField(null=True, blank=True)
    coklat = models.IntegerField(null=True, blank=True)
    merah = models.IntegerField(null=True, blank=True)
    hitam = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    nihil = models.IntegerField(null=True, blank=True)
    periode = models.CharField(max_length=20, blank=True, null=True)
    year = models.IntegerField(null=True, blank=True)
    upload_at = models.DateTimeField(null=True, blank=True)


class BelaDiriMiliter(models.Model):
    nrp = models.ForeignKey('Personil', on_delete=models.CASCADE,
                            related_name='nrp_bdm', null=True, blank=True)
    belt = models.CharField(max_length=50, null=True, blank=True)
    information = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(
        OpsCustomuser, on_delete=models.CASCADE, related_name='creator_bdm', null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    periode = models.CharField(max_length=20, blank=True, null=True)
    is_latest = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    rank = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    organization = models.ForeignKey(
        OpsOrganization, on_delete=models.CASCADE, null=True, blank=True)

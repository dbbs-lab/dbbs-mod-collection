import os

__version__ = "2.0.0"

class Package:
  def __init__(self):
    self.mods = []

class Mod:
  pass

def package():
  pkg = Package()
  pkg.path = os.path.dirname(__file__)
  pkg.name = os.path.basename(pkg.path)
  pkg.astro_version = "0.0.4"
  pkg.glia_version = "0.1.1"
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Ca__granule_cell
  mod_glia__dbbs_mod_collection__Ca__granule_cell = Mod()
  mod_glia__dbbs_mod_collection__Ca__granule_cell.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Ca__granule_cell.asset_name = 'Ca'
  mod_glia__dbbs_mod_collection__Ca__granule_cell.variant = 'granule_cell'
  mod_glia__dbbs_mod_collection__Ca__granule_cell.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Ca__granule_cell.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Ca__granule_cell)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Cav2_2__0
  mod_glia__dbbs_mod_collection__Cav2_2__0 = Mod()
  mod_glia__dbbs_mod_collection__Cav2_2__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Cav2_2__0.asset_name = 'Cav2_2'
  mod_glia__dbbs_mod_collection__Cav2_2__0.variant = '0'
  mod_glia__dbbs_mod_collection__Cav2_2__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Cav2_2__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Cav2_2__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Cav2_3__0
  mod_glia__dbbs_mod_collection__Cav2_3__0 = Mod()
  mod_glia__dbbs_mod_collection__Cav2_3__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Cav2_3__0.asset_name = 'Cav2_3'
  mod_glia__dbbs_mod_collection__Cav2_3__0.variant = '0'
  mod_glia__dbbs_mod_collection__Cav2_3__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Cav2_3__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Cav2_3__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Cav3_1__0
  mod_glia__dbbs_mod_collection__Cav3_1__0 = Mod()
  mod_glia__dbbs_mod_collection__Cav3_1__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Cav3_1__0.asset_name = 'Cav3_1'
  mod_glia__dbbs_mod_collection__Cav3_1__0.variant = '0'
  mod_glia__dbbs_mod_collection__Cav3_1__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Cav3_1__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Cav3_1__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__cdp5__0
  mod_glia__dbbs_mod_collection__cdp5__0 = Mod()
  mod_glia__dbbs_mod_collection__cdp5__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__cdp5__0.asset_name = 'cdp5'
  mod_glia__dbbs_mod_collection__cdp5__0.variant = '0'
  mod_glia__dbbs_mod_collection__cdp5__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__cdp5__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__cdp5__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__cdp5__CR
  mod_glia__dbbs_mod_collection__cdp5__CR = Mod()
  mod_glia__dbbs_mod_collection__cdp5__CR.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__cdp5__CR.asset_name = 'cdp5'
  mod_glia__dbbs_mod_collection__cdp5__CR.variant = 'CR'
  mod_glia__dbbs_mod_collection__cdp5__CR.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__cdp5__CR.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__cdp5__CR)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__HCN1__golgi
  mod_glia__dbbs_mod_collection__HCN1__golgi = Mod()
  mod_glia__dbbs_mod_collection__HCN1__golgi.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__HCN1__golgi.variant = 'golgi'
  mod_glia__dbbs_mod_collection__HCN1__golgi.asset_name = 'HCN1'
  mod_glia__dbbs_mod_collection__HCN1__golgi.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__HCN1__golgi._is_point_process = False
  mod_glia__dbbs_mod_collection__HCN1__golgi._is_artificial_cell = False
  mod_glia__dbbs_mod_collection__HCN1__golgi._name_statement = 'SUFFIX'
  mod_glia__dbbs_mod_collection__HCN1__golgi.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__HCN1__golgi)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__HCN2__0
  mod_glia__dbbs_mod_collection__HCN2__0 = Mod()
  mod_glia__dbbs_mod_collection__HCN2__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__HCN2__0.asset_name = 'HCN2'
  mod_glia__dbbs_mod_collection__HCN2__0.variant = '0'
  mod_glia__dbbs_mod_collection__HCN2__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__HCN2__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__HCN2__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Kca1_1__0
  mod_glia__dbbs_mod_collection__Kca1_1__0 = Mod()
  mod_glia__dbbs_mod_collection__Kca1_1__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kca1_1__0.asset_name = 'Kca1_1'
  mod_glia__dbbs_mod_collection__Kca1_1__0.variant = '0'
  mod_glia__dbbs_mod_collection__Kca1_1__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kca1_1__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Kca1_1__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Kca2_2__0
  mod_glia__dbbs_mod_collection__Kca2_2__0 = Mod()
  mod_glia__dbbs_mod_collection__Kca2_2__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kca2_2__0.asset_name = 'Kca2_2'
  mod_glia__dbbs_mod_collection__Kca2_2__0.variant = '0'
  mod_glia__dbbs_mod_collection__Kca2_2__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kca2_2__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Kca2_2__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Kir2_3__0
  mod_glia__dbbs_mod_collection__Kir2_3__0 = Mod()
  mod_glia__dbbs_mod_collection__Kir2_3__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kir2_3__0.asset_name = 'Kir2_3'
  mod_glia__dbbs_mod_collection__Kir2_3__0.variant = '0'
  mod_glia__dbbs_mod_collection__Kir2_3__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kir2_3__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Kir2_3__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Km__granule_cell
  mod_glia__dbbs_mod_collection__Km__granule_cell = Mod()
  mod_glia__dbbs_mod_collection__Km__granule_cell.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Km__granule_cell.asset_name = 'Km'
  mod_glia__dbbs_mod_collection__Km__granule_cell.variant = 'granule_cell'
  mod_glia__dbbs_mod_collection__Km__granule_cell.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Km__granule_cell.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Km__granule_cell)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Kv7__0
  mod_glia__dbbs_mod_collection__Kv7__0 = Mod()
  mod_glia__dbbs_mod_collection__Kv7__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv7__0.asset_name = 'Kv7'
  mod_glia__dbbs_mod_collection__Kv7__0.variant = '0'
  mod_glia__dbbs_mod_collection__Kv7__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv7__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Kv7__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Kv1_1__0
  mod_glia__dbbs_mod_collection__Kv1_1__0 = Mod()
  mod_glia__dbbs_mod_collection__Kv1_1__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv1_1__0.asset_name = 'Kv1_1'
  mod_glia__dbbs_mod_collection__Kv1_1__0.variant = '0'
  mod_glia__dbbs_mod_collection__Kv1_1__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv1_1__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Kv1_1__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Kv1_5__0
  mod_glia__dbbs_mod_collection__Kv1_5__0 = Mod()
  mod_glia__dbbs_mod_collection__Kv1_5__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv1_5__0.asset_name = 'Kv1_5'
  mod_glia__dbbs_mod_collection__Kv1_5__0.variant = '0'
  mod_glia__dbbs_mod_collection__Kv1_5__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv1_5__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Kv1_5__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Kv2_2__0
  mod_glia__dbbs_mod_collection__Kv2_2__0 = Mod()
  mod_glia__dbbs_mod_collection__Kv2_2__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv2_2__0.asset_name = 'Kv2_2'
  mod_glia__dbbs_mod_collection__Kv2_2__0.variant = '0'
  mod_glia__dbbs_mod_collection__Kv2_2__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv2_2__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Kv2_2__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Kv3_3__0
  mod_glia__dbbs_mod_collection__Kv3_3__0 = Mod()
  mod_glia__dbbs_mod_collection__Kv3_3__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv3_3__0.asset_name = 'Kv3_3'
  mod_glia__dbbs_mod_collection__Kv3_3__0.variant = '0'
  mod_glia__dbbs_mod_collection__Kv3_3__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv3_3__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Kv3_3__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Kv3_4__0
  mod_glia__dbbs_mod_collection__Kv3_4__0 = Mod()
  mod_glia__dbbs_mod_collection__Kv3_4__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv3_4__0.asset_name = 'Kv3_4'
  mod_glia__dbbs_mod_collection__Kv3_4__0.variant = '0'
  mod_glia__dbbs_mod_collection__Kv3_4__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv3_4__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Kv3_4__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Kv4_3__0
  mod_glia__dbbs_mod_collection__Kv4_3__0 = Mod()
  mod_glia__dbbs_mod_collection__Kv4_3__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv4_3__0.asset_name = 'Kv4_3'
  mod_glia__dbbs_mod_collection__Kv4_3__0.variant = '0'
  mod_glia__dbbs_mod_collection__Kv4_3__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kv4_3__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Kv4_3__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Leak__0
  mod_glia__dbbs_mod_collection__Leak__0 = Mod()
  mod_glia__dbbs_mod_collection__Leak__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Leak__0.asset_name = 'Leak'
  mod_glia__dbbs_mod_collection__Leak__0.variant = '0'
  mod_glia__dbbs_mod_collection__Leak__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Leak__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Leak__0)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Na__granule_cell
  mod_glia__dbbs_mod_collection__Na__granule_cell = Mod()
  mod_glia__dbbs_mod_collection__Na__granule_cell.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Na__granule_cell.asset_name = 'Na'
  mod_glia__dbbs_mod_collection__Na__granule_cell.variant = 'granule_cell'
  mod_glia__dbbs_mod_collection__Na__granule_cell.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Na__granule_cell.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Na__granule_cell)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Na__granule_cell_FHF
  mod_glia__dbbs_mod_collection__Na__granule_cell_FHF = Mod()
  mod_glia__dbbs_mod_collection__Na__granule_cell_FHF.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Na__granule_cell_FHF.asset_name = 'Na'
  mod_glia__dbbs_mod_collection__Na__granule_cell_FHF.variant = 'granule_cell_FHF'
  mod_glia__dbbs_mod_collection__Na__granule_cell_FHF.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Na__granule_cell_FHF.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Na__granule_cell_FHF)
  #-##
  #-Generated by Astrocyte v0.0.4
  #-mod_glia__dbbs_mod_collection__Nav1_6__0
  mod_glia__dbbs_mod_collection__Nav1_6__0 = Mod()
  mod_glia__dbbs_mod_collection__Nav1_6__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Nav1_6__0.asset_name = 'Nav1_6'
  mod_glia__dbbs_mod_collection__Nav1_6__0.variant = '0'
  mod_glia__dbbs_mod_collection__Nav1_6__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Nav1_6__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Nav1_6__0)
  #-##
  #-Generated by Astrocyte v0.0.5
  #-mod_glia__dbbs_mod_collection__AMPA__granule
  mod_glia__dbbs_mod_collection__AMPA__granule = Mod()
  mod_glia__dbbs_mod_collection__AMPA__granule.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__AMPA__granule.asset_name = 'AMPA'
  mod_glia__dbbs_mod_collection__AMPA__granule.variant = 'granule'
  mod_glia__dbbs_mod_collection__AMPA__granule.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__AMPA__granule._is_point_process = True
  mod_glia__dbbs_mod_collection__AMPA__granule._is_artificial_cell = False
  mod_glia__dbbs_mod_collection__AMPA__granule._name_statement = 'POINT_PROCESS'
  mod_glia__dbbs_mod_collection__AMPA__granule.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__AMPA__granule)
  #-##
  #-Generated by Astrocyte v0.0.5
  #-mod_glia__dbbs_mod_collection__GABA__granule
  mod_glia__dbbs_mod_collection__GABA__granule = Mod()
  mod_glia__dbbs_mod_collection__GABA__granule.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__GABA__granule.asset_name = 'GABA'
  mod_glia__dbbs_mod_collection__GABA__granule.variant = 'granule'
  mod_glia__dbbs_mod_collection__GABA__granule.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__GABA__granule._is_point_process = True
  mod_glia__dbbs_mod_collection__GABA__granule._is_artificial_cell = False
  mod_glia__dbbs_mod_collection__GABA__granule._name_statement = 'POINT_PROCESS'
  mod_glia__dbbs_mod_collection__GABA__granule.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__GABA__granule)
  #-##
  #-Generated by Astrocyte v0.0.5
  #-mod_glia__dbbs_mod_collection__NMDA__granule
  mod_glia__dbbs_mod_collection__NMDA__granule = Mod()
  mod_glia__dbbs_mod_collection__NMDA__granule.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__NMDA__granule.asset_name = 'NMDA'
  mod_glia__dbbs_mod_collection__NMDA__granule.variant = 'granule'
  mod_glia__dbbs_mod_collection__NMDA__granule.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__NMDA__granule._is_point_process = True
  mod_glia__dbbs_mod_collection__NMDA__granule._is_artificial_cell = False
  mod_glia__dbbs_mod_collection__NMDA__granule._name_statement = 'POINT_PROCESS'
  mod_glia__dbbs_mod_collection__NMDA__granule.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__NMDA__granule)
  #-##
  #-Generated by Astrocyte v0.2.0
  #-mod_glia__dbbs_mod_collection__AMPA__0
  mod_glia__dbbs_mod_collection__AMPA__0 = Mod()
  mod_glia__dbbs_mod_collection__AMPA__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__AMPA__0.asset_name = 'AMPA'
  mod_glia__dbbs_mod_collection__AMPA__0.variant = '0'
  mod_glia__dbbs_mod_collection__AMPA__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__AMPA__0._is_point_process = True
  mod_glia__dbbs_mod_collection__AMPA__0._is_artificial_cell = False
  mod_glia__dbbs_mod_collection__AMPA__0._name_statement = 'POINT_PROCESS'
  mod_glia__dbbs_mod_collection__AMPA__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__AMPA__0)
  #-##
  #-Generated by Astrocyte v0.2.0
  #-mod_glia__dbbs_mod_collection__Nav1_1__0
  mod_glia__dbbs_mod_collection__Nav1_1__0 = Mod()
  mod_glia__dbbs_mod_collection__Nav1_1__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Nav1_1__0.asset_name = 'Nav1_1'
  mod_glia__dbbs_mod_collection__Nav1_1__0.variant = '0'
  mod_glia__dbbs_mod_collection__Nav1_1__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Nav1_1__0._is_point_process = False
  mod_glia__dbbs_mod_collection__Nav1_1__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Nav1_1__0)
  #-##
  #-Generated by Astrocyte v0.2.0
  #-mod_glia__dbbs_mod_collection__NMDA__stellate
  mod_glia__dbbs_mod_collection__NMDA__stellate = Mod()
  mod_glia__dbbs_mod_collection__NMDA__stellate.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__NMDA__stellate.asset_name = 'NMDA'
  mod_glia__dbbs_mod_collection__NMDA__stellate.variant = 'stellate'
  mod_glia__dbbs_mod_collection__NMDA__stellate.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__NMDA__stellate._is_point_process = True
  mod_glia__dbbs_mod_collection__NMDA__stellate.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__NMDA__stellate)
  #-##
  #-Generated by Astrocyte v0.2.1
  #-mod_glia__dbbs_mod_collection__Cav3_2__0
  mod_glia__dbbs_mod_collection__Cav3_2__0 = Mod()
  mod_glia__dbbs_mod_collection__Cav3_2__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Cav3_2__0.asset_name = 'Cav3_2'
  mod_glia__dbbs_mod_collection__Cav3_2__0.variant = '0'
  mod_glia__dbbs_mod_collection__Cav3_2__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Cav3_2__0._is_point_process = False
  mod_glia__dbbs_mod_collection__Cav3_2__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Cav3_2__0)
  #-##
  #-Generated by Astrocyte v0.2.1
  #-mod_glia__dbbs_mod_collection__Cav3_3__0
  mod_glia__dbbs_mod_collection__Cav3_3__0 = Mod()
  mod_glia__dbbs_mod_collection__Cav3_3__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Cav3_3__0.asset_name = 'Cav3_3'
  mod_glia__dbbs_mod_collection__Cav3_3__0.variant = '0'
  mod_glia__dbbs_mod_collection__Cav3_3__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Cav3_3__0._is_point_process = False
  mod_glia__dbbs_mod_collection__Cav3_3__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Cav3_3__0)
  #-##
  #-Generated by Astrocyte v0.2.1
  #-mod_glia__dbbs_mod_collection__Cav2_1__0
  mod_glia__dbbs_mod_collection__Cav2_1__0 = Mod()
  mod_glia__dbbs_mod_collection__Cav2_1__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Cav2_1__0.asset_name = 'Cav2_1'
  mod_glia__dbbs_mod_collection__Cav2_1__0.variant = '0'
  mod_glia__dbbs_mod_collection__Cav2_1__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Cav2_1__0._is_point_process = False
  mod_glia__dbbs_mod_collection__Cav2_1__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Cav2_1__0)
  #-##
  #-Generated by Astrocyte v0.2.1
  #-mod_glia__dbbs_mod_collection__HCN1__0
  mod_glia__dbbs_mod_collection__HCN1__0 = Mod()
  mod_glia__dbbs_mod_collection__HCN1__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__HCN1__0.asset_name = 'HCN1'
  mod_glia__dbbs_mod_collection__HCN1__0.variant = '0'
  mod_glia__dbbs_mod_collection__HCN1__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__HCN1__0._is_point_process = False
  mod_glia__dbbs_mod_collection__HCN1__0._is_artificial_cell = False
  mod_glia__dbbs_mod_collection__HCN1__0._name_statement = 'SUFFIX'
  mod_glia__dbbs_mod_collection__HCN1__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__HCN1__0)
  #-##
  #-Generated by Astrocyte v0.2.0
  #-mod_glia__dbbs_mod_collection__Kca3_1__0
  mod_glia__dbbs_mod_collection__Kca3_1__0 = Mod()
  mod_glia__dbbs_mod_collection__Kca3_1__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kca3_1__0.asset_name = 'Kca3_1'
  mod_glia__dbbs_mod_collection__Kca3_1__0.variant = '0'
  mod_glia__dbbs_mod_collection__Kca3_1__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Kca3_1__0._is_point_process = False
  mod_glia__dbbs_mod_collection__Kca3_1__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Kca3_1__0)
  #-##
  #-Generated by Astrocyte v0.2.0
  #-mod_glia__dbbs_mod_collection__cdp5__CAM
  mod_glia__dbbs_mod_collection__cdp5__CAM = Mod()
  mod_glia__dbbs_mod_collection__cdp5__CAM.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__cdp5__CAM.asset_name = 'cdp5'
  mod_glia__dbbs_mod_collection__cdp5__CAM.variant = 'CAM'
  mod_glia__dbbs_mod_collection__cdp5__CAM.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__cdp5__CAM._is_point_process = False
  mod_glia__dbbs_mod_collection__cdp5__CAM.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__cdp5__CAM)
  #-##
  #-Generated by Astrocyte v0.2.3
  #-mod_glia__dbbs_mod_collection__CaL13__0
  mod_glia__dbbs_mod_collection__CaL13__0 = Mod()
  mod_glia__dbbs_mod_collection__CaL13__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__CaL13__0.asset_name = 'CaL13'
  mod_glia__dbbs_mod_collection__CaL13__0.variant = '0'
  mod_glia__dbbs_mod_collection__CaL13__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__CaL13__0._is_point_process = False
  mod_glia__dbbs_mod_collection__CaL13__0._is_artificial_cell = False
  mod_glia__dbbs_mod_collection__CaL13__0._name_statement = 'SUFFIX'
  mod_glia__dbbs_mod_collection__CaL13__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__CaL13__0)
  #-##
  #-Generated by Astrocyte v0.2.4
  #-mod_glia__dbbs_mod_collection__GABA__0
  mod_glia__dbbs_mod_collection__GABA__0 = Mod()
  mod_glia__dbbs_mod_collection__GABA__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__GABA__0.asset_name = 'GABA'
  mod_glia__dbbs_mod_collection__GABA__0.variant = '0'
  mod_glia__dbbs_mod_collection__GABA__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__GABA__0._is_point_process = True
  mod_glia__dbbs_mod_collection__GABA__0._is_artificial_cell = False
  mod_glia__dbbs_mod_collection__GABA__0._name_statement = 'POINT_PROCESS'
  mod_glia__dbbs_mod_collection__GABA__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__GABA__0)
  #-##
  #-Generated by Astrocyte v0.2.4
  #-mod_glia__dbbs_mod_collection__cdp5__CAM_GoC
  mod_glia__dbbs_mod_collection__cdp5__CAM_GoC = Mod()
  mod_glia__dbbs_mod_collection__cdp5__CAM_GoC.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__cdp5__CAM_GoC.asset_name = 'cdp5'
  mod_glia__dbbs_mod_collection__cdp5__CAM_GoC.variant = 'CAM_GoC'
  mod_glia__dbbs_mod_collection__cdp5__CAM_GoC.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__cdp5__CAM_GoC._is_point_process = False
  mod_glia__dbbs_mod_collection__cdp5__CAM_GoC._is_artificial_cell = False
  mod_glia__dbbs_mod_collection__cdp5__CAM_GoC._name_statement = 'SUFFIX'
  mod_glia__dbbs_mod_collection__cdp5__CAM_GoC.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__cdp5__CAM_GoC)
  #-##
  #-Generated by Astrocyte v0.2.3
  #-mod_glia__dbbs_mod_collection__GABA__biexp
  mod_glia__dbbs_mod_collection__GABA__biexp = Mod()
  mod_glia__dbbs_mod_collection__GABA__biexp.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__GABA__biexp.asset_name = 'GABA'
  mod_glia__dbbs_mod_collection__GABA__biexp.variant = 'biexp'
  mod_glia__dbbs_mod_collection__GABA__biexp.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__GABA__biexp._is_point_process = True
  mod_glia__dbbs_mod_collection__GABA__biexp._is_artificial_cell = False
  mod_glia__dbbs_mod_collection__GABA__biexp._name_statement = 'POINT_PROCESS'
  mod_glia__dbbs_mod_collection__GABA__biexp.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__GABA__biexp)
  #-##
  #-Generated by Astrocyte v0.2.3
  #-mod_glia__dbbs_mod_collection__Leak__GABA
  mod_glia__dbbs_mod_collection__Leak__GABA = Mod()
  mod_glia__dbbs_mod_collection__Leak__GABA.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Leak__GABA.asset_name = 'Leak'
  mod_glia__dbbs_mod_collection__Leak__GABA.variant = 'GABA'
  mod_glia__dbbs_mod_collection__Leak__GABA.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__Leak__GABA._is_point_process = False
  mod_glia__dbbs_mod_collection__Leak__GABA._is_artificial_cell = False
  mod_glia__dbbs_mod_collection__Leak__GABA._name_statement = 'SUFFIX'
  mod_glia__dbbs_mod_collection__Leak__GABA.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__Leak__GABA)
  #-##
  #-Generated by Astrocyte v0.2.3
  #-mod_glia__dbbs_mod_collection__gap_junction__0
  mod_glia__dbbs_mod_collection__gap_junction__0 = Mod()
  mod_glia__dbbs_mod_collection__gap_junction__0.pkg_name = 'dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__gap_junction__0.asset_name = 'gap_junction'
  mod_glia__dbbs_mod_collection__gap_junction__0.variant = '0'
  mod_glia__dbbs_mod_collection__gap_junction__0.namespace = 'glia__dbbs_mod_collection'
  mod_glia__dbbs_mod_collection__gap_junction__0._is_point_process = True
  mod_glia__dbbs_mod_collection__gap_junction__0._is_artificial_cell = False
  mod_glia__dbbs_mod_collection__gap_junction__0._name_statement = 'POINT_PROCESS'
  mod_glia__dbbs_mod_collection__gap_junction__0.pkg = pkg
  pkg.mods.append(mod_glia__dbbs_mod_collection__gap_junction__0)
  #-##
  return pkg

from pxr import UsdShade

def get_material_prim(stage, mesh_prim):
    """
    从mesh prim获取绑定的材质material prim
    先获取material prim_path
    再获取UsdShade.Material对象
    最后获取material prim
    """
    material_bing_api = UsdShade.MaterialBindingAPI(mesh_prim)
    if material_bing_api:
        material_prim_path = material_bing_api.GetDirectBindingRel().GetTargets()[0]
        usd_shade_material = UsdShade.Material.Get(stage, material_prim_path)
        material_prim = usd_shade_material.GetPrim()
        return material_prim

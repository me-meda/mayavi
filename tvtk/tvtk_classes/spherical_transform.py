# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.warp_transform import WarpTransform


class SphericalTransform(WarpTransform):
    """
    SphericalTransform - spherical to rectangular coords and back
    
    Superclass: WarpTransform
    
    SphericalTransform will convert (r,phi,theta) coordinates to
    (x,y,z) coordinates and back again.  The angles are given in radians.
    By default, it converts spherical coordinates to rectangular, but
    get_inverse() returns a transform that will do the opposite.  The
    equation that is used is x = r*sin(phi)*cos(theta), y =
    r*sin(phi)*sin(theta), z = r*cos(phi).
    
    Caveats:
    
    This transform is not well behaved along the line x=y=0 (i.e. along
    the z-axis)
    
    See Also:
    
    CylindricalTransform GeneralTransform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSphericalTransform, obj, update, **traits)
    
    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('inverse_iterations',
    'GetInverseIterations'), ('inverse_tolerance', 'GetInverseTolerance'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'inverse_iterations',
    'inverse_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SphericalTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SphericalTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['inverse_iterations', 'inverse_tolerance']),
            title='Edit SphericalTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SphericalTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


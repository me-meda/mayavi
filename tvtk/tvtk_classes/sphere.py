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

from tvtk.tvtk_classes.implicit_function import ImplicitFunction


class Sphere(ImplicitFunction):
    """
    Sphere - implicit function for a sphere
    
    Superclass: ImplicitFunction
    
    Sphere computes the implicit function and/or gradient for a
    sphere. Sphere is a concrete implementation of
    ImplicitFunction. Additional methods are available for
    sphere-related computations, such as computing bounding spheres for a
    set of points, or set of spheres.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSphere, obj, update, **traits)
    
    radius = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set / get the radius of the sphere. The default is 0.5.
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('radius', 'GetRadius'), ('center', 'GetCenter'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'center', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Sphere, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Sphere properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['center', 'radius']),
            title='Edit Sphere properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Sphere properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


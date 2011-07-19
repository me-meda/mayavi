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

from tvtk.tvtk_classes.parametric_function import ParametricFunction


class ParametricBoy(ParametricFunction):
    """
    ParametricBoy - Generate Boy's surface.
    
    Superclass: ParametricFunction
    
    ParametricBoy generates Boy's surface. This is a Model of the
    projective plane without singularities. It was found by Werner Boy on
    assignment from David Hilbert.
    
    For further information about this surface, please consult the
    technical description "Parametric surfaces" in
    http://www.vtk.org/documents.php in the "VTK Technical Documents"
    section in the VTk.org web pages.
    
    Thanks:
    
    Andrew Maclean a.maclean@cas.edu.au for creating and contributing the
    class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParametricBoy, obj, update, **traits)
    
    z_scale = traits.Float(0.125, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scale factor for the z-coordinate. Default = 1/8,
        giving a nice shape.
        """
    )
    def _z_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZScale,
                        self.z_scale)

    _updateable_traits_ = \
    (('clockwise_ordering', 'GetClockwiseOrdering'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('derivatives_available', 'GetDerivativesAvailable'),
    ('join_v', 'GetJoinV'), ('join_u', 'GetJoinU'), ('twist_v',
    'GetTwistV'), ('twist_u', 'GetTwistU'), ('minimum_u', 'GetMinimumU'),
    ('minimum_v', 'GetMinimumV'), ('minimum_w', 'GetMinimumW'),
    ('reference_count', 'GetReferenceCount'), ('maximum_v',
    'GetMaximumV'), ('maximum_w', 'GetMaximumW'), ('z_scale',
    'GetZScale'), ('maximum_u', 'GetMaximumU'))
    
    _full_traitnames_list_ = \
    (['clockwise_ordering', 'debug', 'derivatives_available',
    'global_warning_display', 'join_u', 'join_v', 'twist_u', 'twist_v',
    'maximum_u', 'maximum_v', 'maximum_w', 'minimum_u', 'minimum_v',
    'minimum_w', 'z_scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParametricBoy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ParametricBoy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['clockwise_ordering', 'derivatives_available',
            'join_u', 'join_v', 'twist_u', 'twist_v'], [], ['maximum_u',
            'maximum_v', 'maximum_w', 'minimum_u', 'minimum_v', 'minimum_w',
            'z_scale']),
            title='Edit ParametricBoy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParametricBoy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


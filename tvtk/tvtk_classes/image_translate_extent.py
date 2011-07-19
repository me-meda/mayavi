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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageTranslateExtent(ImageAlgorithm):
    """
    ImageTranslateExtent - Changes extent, nothing else.
    
    Superclass: ImageAlgorithm
    
    ImageTranslateExtent  shift the whole extent, but does not change
    the data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageTranslateExtent, obj, update, **traits)
    
    translation = traits.Array(shape=(3,), value=(0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslation,
                        self.translation)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('translation', 'GetTranslation'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'translation'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageTranslateExtent, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageTranslateExtent properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['translation']),
            title='Edit ImageTranslateExtent properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageTranslateExtent properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

